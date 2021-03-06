"""
  questions to ask:
  - will word1 == word2?
  - will either word1, word2 be in the list always? 
"""

"""
    naive solution: brute force O(n^2)
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int

        1st approach: 2pointers

        Time    O(n)
        Space   O(n)
        52 ms, faster than 27.57%
        """
        p1 = -1
        p2 = -1
        res = len(words)
        for i in range(len(words)):
            word = words[i]
            if word == word1:
                p1 = i
            if word == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                res = min(res, abs(p1-p2))
        return res


a = ["practice", "makes", "perfect", "coding", "makes"]
b = "makes"
c = "coding"
print(Solution().shortestDistance(a, b, c))
