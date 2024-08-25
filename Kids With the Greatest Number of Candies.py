# 1431. Kids With the Greatest Number of Candies

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        highest = max(candies)
        is_greatest = []

        for i in range(n):
            result = candies[i] + extraCandies
            is_greatest.append(result>=highest)
        return is_greatest