import math
from functools import lru_cache
from typing import List, Dict, Tuple

class DiceStatistics:
    @staticmethod
    def calculate_probability(target: int, num_dice: int, num_faces: int) -> float:
        """
        Calculate the probability of rolling target or higher.

        Args:
            target (int): Target sum to calculate probability for
            num_dice (int): Number of dice
            num_faces (int): Number of faces per die

        Returns:
            float: Probability of rolling the target sum or higher (0-1)
        """
        total_outcomes = num_faces ** num_dice
        favorable_outcomes = sum(
            DiceStatistics._ways_to_roll_sum(i, num_dice, num_faces)
            for i in range(target, (num_dice * num_faces) + 1)
        )

        return favorable_outcomes / total_outcomes

    @staticmethod
    @lru_cache(maxsize=None)  # Memoization to cache previous calculations
    def _ways_to_roll_sum(target: int, num_dice: int, num_faces: int) -> int:
        """
        Efficiently calculate ways to roll a specific sum using recursion + memoization.

        Args:
            target (int): Target sum
            num_dice (int): Number of dice
            num_faces (int): Number of faces per die

        Returns:
            int: Number of ways to roll the target sum
        """
        if target < num_dice or target > num_dice * num_faces:
            return 0  # Impossible case

        if num_dice == 1:
            return 1 if 1 <= target <= num_faces else 0

        # Recursively calculate ways for smaller subproblems
        return sum(
            DiceStatistics._ways_to_roll_sum(target - face, num_dice - 1, num_faces)
            for face in range(1, num_faces + 1)
        )

    @staticmethod
    def get_probability_range(num_dice: int, num_faces: int) -> Dict[str, float]:
        """
        Calculate basic probability statistics for the roll.

        Args:
            num_dice (int): Number of dice
            num_faces (int): Number of faces per die

        Returns:
            Dict[str, float]: Dictionary containing probability statistics
        """
        mean = num_dice * (num_faces + 1) / 2
        variance = num_dice * ((num_faces ** 2 - 1) / 12)
        std_dev = math.sqrt(variance)

        return {
            "mean": mean,
            "std_dev": std_dev
        }

    @staticmethod
    def analyze_rolls(rolls: List[int]) -> Dict[str, float]:
        """
        Analyze a list of roll results.

        Args:
            rolls (List[int]): List of roll results

        Returns:
            Dict[str, float]: Dictionary containing roll statistics
        """
        if not rolls:
            return {}

        return {
            "mean": sum(rolls) / len(rolls),
            "min": min(rolls),
            "max": max(rolls),
            "count": len(rolls)
        }
