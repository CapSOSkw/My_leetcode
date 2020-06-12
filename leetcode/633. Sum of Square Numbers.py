'''
Given a non-negative integer c, your task is to decide whether
there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
'''
from math import sqrt

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        while a * a <= c:
            if sqrt(c - a*a) % 1 == 0:
                return True
            a += 1
        else:
            return False



s = Solution()

for x in range(1, 200):
    print(x, s.judgeSquareSum(x))
# s.judgeSquareSum(8)