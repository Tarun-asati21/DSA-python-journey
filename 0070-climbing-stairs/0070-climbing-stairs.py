import math


class Solution:

  def climbStairs(self, n: int) -> int:
    total_ways = 0

    # y is the number of 2-step moves, ranging from 0 up to n // 2
    for y in range(0, n // 2 + 1):
      x = n - 2 * y  # number of 1-step moves
      total_moves = x + y  # total number of moves (n - y)

      # Combinations formula: C(total_moves, y) = total_moves! / (y! * (total_moves - y)!)
      ways = math.comb(total_moves, y)
      total_ways += ways

    return total_ways