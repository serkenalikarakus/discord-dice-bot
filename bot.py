import discord
from discord.ext import commands
import re
from dice_roller import DiceRoller
from dice_statistics import DiceStatistics
from config import (
    PREFIX, ROLL_COMMAND, DICE_HELP_COMMAND,
    ERROR_INVALID_FORMAT, HELP_MESSAGE
)

# Create bot instance with required intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(
    command_prefix=PREFIX,
    help_command=None,
    intents=intents
)

# Create instances
dice_roller = DiceRoller()
dice_stats = DiceStatistics()

@bot.event
async def on_ready():
    """Event handler for when the bot is ready and connected to Discord."""
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is ready with prefix: {PREFIX}')
    await bot.change_presence(activity=discord.Game(name=f"{PREFIX}{DICE_HELP_COMMAND} for commands"))

@bot.command(name=ROLL_COMMAND)
async def roll(ctx, *, dice_str: str):
    """
    Command to roll dice based on the input string format NdM.
    """
    print(f"Roll command received: {dice_str}")

    # Parse input using regex
    match = re.match(r'^(\d+)d(\d+)$', dice_str.lower())

    if not match:
        print(f"Invalid format: {dice_str}")
        await ctx.send(ERROR_INVALID_FORMAT)
        return

    try:
        num_dice = int(match.group(1))
        num_faces = int(match.group(2))
    except ValueError:
        print(f"Value error parsing: {dice_str}")
        await ctx.send(ERROR_INVALID_FORMAT)
        return

    # Validate input
    is_valid, error_message = dice_roller.validate_input(num_dice, num_faces)
    if not is_valid:
        print(f"Validation failed: {error_message}")
        await ctx.send(error_message)
        return

    # Roll dice and format result
    rolls, total = dice_roller.roll_dice(num_dice, num_faces)
    result = dice_roller.format_roll_result(rolls, total)

    # Get statistical analysis
    stats = dice_stats.get_probability_range(num_dice, num_faces)

    # Determine roll quality
    quality = "Average"
    if total > stats['mean'] + stats['std_dev']:
        quality = "High"
    elif total < stats['mean'] - stats['std_dev']:
        quality = "Low"

    # Calculate probability of this roll or better
    prob = dice_stats.calculate_probability(total, num_dice, num_faces)
    prob_percentage = prob * 100

    # Create and send embed
    embed = discord.Embed(
        title=f"Rolling {num_dice}d{num_faces}",
        description=result,
        color=discord.Color.blue()
    )

    embed.add_field(
        name="Roll Analysis",
        value=f"Roll Quality: {quality}\n"
              f"Probability of this roll or better: {prob_percentage:.1f}%",
        inline=False
    )

    embed.set_footer(text=f"Requested by {ctx.author.name}")

    await ctx.send(embed=embed)
    print(f"Roll completed: {result}")

@bot.command(name="probability")
async def probability(ctx, *, args: str):
    """Calculate probability of rolling a specific total."""
    match = re.match(r'^(\d+)d(\d+)\s+(\d+)$', args.lower())

    if not match:
        await ctx.send("Invalid format! Use: !probability NdM X (e.g., !probability 2d6 7)")
        return

    try:
        num_dice = int(match.group(1))
        num_faces = int(match.group(2))
        target = int(match.group(3))
    except ValueError:
        await ctx.send("Invalid numbers provided!")
        return

    # Validate input
    is_valid, error_message = dice_roller.validate_input(num_dice, num_faces)
    if not is_valid:
        await ctx.send(error_message)
        return

    # Calculate probability
    prob = dice_stats.calculate_probability(target, num_dice, num_faces)
    percentage = prob * 100

    embed = discord.Embed(
        title=f"Probability Analysis for {num_dice}d{num_faces}",
        description=f"Chance of rolling {target} or higher: {percentage:.2f}%",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

@bot.command(name=DICE_HELP_COMMAND)
async def dice_help(ctx):  
    """Command to display help information."""
    print(f"Help command received from {ctx.author.name}")
    help_text = HELP_MESSAGE + "\n\n**Statistics Commands:**\n"
    help_text += f"`{PREFIX}probability NdM X` - Calculate probability of rolling X with NdM dice\n"

    embed = discord.Embed(
        title="Dice Roller Bot Help",
        description=help_text,
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)
    print("Help message sent")

@bot.event
async def on_command_error(ctx, error):
    """Global error handler for bot commands."""
    print(f"Command error occurred: {str(error)}")
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(ERROR_INVALID_FORMAT)
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send(f"Unknown command. Use {PREFIX}{DICE_HELP_COMMAND} for available commands.")
    else:
        await ctx.send(f"An error occurred: {str(error)}")

# Run the bot (token should be provided as environment variable)
if __name__ == "__main__":
    import os
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        print("Error: DISCORD_TOKEN environment variable not set")
        exit(1)
    bot.run(TOKEN)