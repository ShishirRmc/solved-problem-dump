# 1431. Kids With the Greatest Number of Candies

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Get the number of children
        n = len(candies)
        
        # Find the highest number of candies any kid currently has
        highest = max(candies)
        
        # Initialize an empty list to store the boolean results
        is_greatest = []

        # Iterate through each child's candy count
        for i in range(n):
            # Calculate the total candies if the child receives extraCandies
            result = candies[i] + extraCandies
            
            # Check if the total candies are greater than or equal to the highest
            # Append True if it is, otherwise append False
            is_greatest.append(result >= highest)
        
        # Return the list of boolean values
        return is_greatest

# n
# pratek ko lagi, result = candies[i] + extraCandies
# if result >= max(candies): then return true or false