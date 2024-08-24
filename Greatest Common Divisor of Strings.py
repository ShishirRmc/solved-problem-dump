# leetcode problem, 1071. Greatest Common Divisor of Strings

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 + str2 is equal to str2 + str1
        # If not, the strings cannot be formed from the same substring
        if str1 + str2 != str2 + str1:
            return ""

        # Compute the greatest common divisor (GCD) of the lengths of str1 and str2
        gcd1 = gcd(len(str1), len(str2))

        # Determine the longer string and use it to extract the GCD substring
        if len(str1) > len(str2):
            high = str1
        else:
            high = str2

        # Return the substring of length gcd1 from the longer string
        return high[:gcd1]
