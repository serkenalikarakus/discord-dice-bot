import math
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
        favorable_outcomes = 0

        # For efficiency, calculate probability for target or higher
        for i in range(target, (num_dice * num_faces) + 1):
            ways = DiceStatistics._ways_to_roll_sum(i, num_dice, num_faces)
            favorable_outcomes += ways

        return favorable_outcomes / total_outcomes

    @staticmethod
    def _ways_to_roll_sum(target: int, num_dice: int, num_faces: int) -> int:
        """Helper method to calculate ways to roll a specific sum."""
        if num_dice == 1:
            return 1 if 1 <= target <= num_faces else 0

        ways = [[0] * (target + 1) for _ in range(num_dice + 1)]
        ways[0][0] = 1

        for i in range(1, num_dice + 1):
            for j in range(i, min(i * num_faces + 1, target + 1)):
                for k in range(1, min(num_faces + 1, j + 1)):
                    ways[i][j] += ways[i-1][j-k]

        return ways[num_dice][target]

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

def erf(x: float) -> float:
    """
    Approximation of the error function for probability calculations.
    """
    a = 8/(3*math.pi) * (math.pi-3)/(4-math.pi)
    return math.copysign(math.sqrt(1 - math.exp(-x*x * (4/math.pi + a*x*x)/(1 + a*x*x))), x)