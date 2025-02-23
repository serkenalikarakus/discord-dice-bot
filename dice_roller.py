import random
from typing import Tuple, List
from config import MAX_DICE, MAX_FACES

class DiceRoller:
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
            return False, "Number of dice and faces must be greater than 0!"
        if num_dice > MAX_DICE:
            return False, f"Cannot roll more than {MAX_DICE} dice at once!"
        if num_faces > MAX_FACES:
            return False, f"Dice cannot have more than {MAX_FACES} faces!"
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
        # Single roll implementation
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
        rolls_str = ', '.join(str(r) for r in rolls)
        return f"Rolls: [{rolls_str}]\nTotal: {total}"
