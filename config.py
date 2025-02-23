# Configuration settings for the Discord bot

# Command prefix for the bot
PREFIX = '!'

# Maximum limits
MAX_DICE = 100
MAX_FACES = 100

# Bot command settings
ROLL_COMMAND = 'roll'
DICE_HELP_COMMAND = 'dicehelp'  # Changed from HELP_COMMAND to DICE_HELP_COMMAND

# Error messages
ERROR_TOO_MANY_DICE = f"Error: Cannot roll more than {MAX_DICE} dice at once!"
ERROR_TOO_MANY_FACES = f"Error: Dice cannot have more than {MAX_FACES} faces!"
ERROR_INVALID_FORMAT = "Error: Invalid format! Use: !roll NdM (e.g., !roll 2d6)"
ERROR_NEGATIVE_VALUES = "Error: Number of dice and faces must be positive!"
ERROR_ZERO_VALUES = "Error: Number of dice and faces must be greater than 0!"

# Help message
HELP_MESSAGE = f"""
**Dice Roller Bot Help**
Roll dice using the following command:
`{PREFIX}{ROLL_COMMAND} NdM`
where:
- N is the number of dice (1-{MAX_DICE})
- d is the separator
- M is the number of faces per die (1-{MAX_FACES})

Example: `{PREFIX}{ROLL_COMMAND} 2d6` rolls two six-sided dice
"""