# Leet code 1768. Merge Strings Alternately
#  got 44.21% beating
# I now its not much, am starting, just use it as a refrence, i don't own the solution

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Determine which word is longer and assign accordingly
        if len(word1) > len(word2):
            high = word1
            low = word2
        else:
            high = word2
            low = word1

        i = 0  # Index for word1
        j = 0  # Index for word2
        ans = ""  # Resultant merged string
        
        # Merge characters from both words alternately
        while i < len(word1) and j < len(word2):
            ans += word1[i] + word2[j]
            i += 1
            j += 1

        # Append the remaining part of the longer word (if any)
        low_l = len(low)
        ans += high[low_l:]
        
        return ans
