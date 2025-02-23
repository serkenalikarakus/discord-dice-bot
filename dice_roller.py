import random
from typing import Tuple, List
from config import CONFIG

class DiceRoller:
    MAX_DICE = 100  # Maximum dice allowed
    MAX_FACES = 100  # Maximum faces per die

    @staticmethod
    def validate_input(num_dice: int, num_faces: int) -> Tuple[bool, str]:
        """
        Validate the input parameters for dice rolling.

        Args:
            num_dice (int): Number of dice
            num_faces (int): Number of faces per die

        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        if num_dice <= 0 or num_faces <= 0:
            return False, CONFIG["ERROR_ZERO_VALUES"]
        if num_dice > DiceRoller.MAX_DICE:
            return False, CONFIG["ERROR_TOO_MANY_DICE"]
        if num_faces > DiceRoller.MAX_FACES:
            return False, CONFIG["ERROR_TOO_MANY_FACES"]
        return True, ""

    @staticmethod
    def roll_dice(num_dice: int, num_faces: int) -> Tuple[List[int], int]:
        """
        Roll the specified number of dice with the given number of faces.

        Args:
            num_dice (int): Number of dice to roll
            num_faces (int): Number of faces per die

        Returns:
            Tuple[List[int], int]: (list of individual rolls, sum of all rolls)
        """
        rolls = [random.randint(1, num_faces) for _ in range(num_dice)]
        return rolls, sum(rolls)

    @staticmethod
    def format_roll_result(rolls: List[int], total: int) -> str:
        """
        Format the roll results into a readable string.

        Args:
            rolls (List[int]): List of individual roll results
            total (int): Sum of all rolls

        Returns:
            str: Formatted result string
        """
        rolls_str = ', '.join(map(str, rolls))
        return f"🎲 Rolls: [{rolls_str}]\n**Total: {total}**"
