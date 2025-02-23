import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def load_config():
    return {
        "TOKEN": os.getenv("DISCORD_TOKEN"),
        "PREFIX": os.getenv("PREFIX", "!"),
        "ROLL_COMMAND": "roll",
        "DICE_HELP_COMMAND": "dicehelp",
        "MAX_DICE": 100,
        "MAX_FACES": 100,
        "ERROR_TOO_MANY_DICE": "Error: Cannot roll more than 100 dice at once!",
        "ERROR_TOO_MANY_FACES": "Error: Dice cannot have more than 100 faces!",
        "ERROR_INVALID_FORMAT": "Error: Invalid format! Use: !roll NdM (e.g., !roll 2d6)",
        "ERROR_NEGATIVE_VALUES": "Error: Number of dice and faces must be positive!",
        "ERROR_ZERO_VALUES": "Error: Number of dice and faces must be greater than 0!",
        "HELP_MESSAGE": """
        **Dice Roller Bot Help**
        Roll dice using the following command:
        `!roll NdM`
        where:
        - N is the number of dice (1-100)
        - d is the separator
        - M is the number of faces per die (1-100)
        
        Example: `!roll 2d6` rolls two six-sided dice
        """
    }

# Load config values
CONFIG = load_config()
