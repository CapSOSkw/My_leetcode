'''

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
'''

'''
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
15! = 1307674368000
20! = 2432902008176640000
25! = 15511210043330985984000000
'''

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)


def factorial(n):
    if n < 0:
        raise ValueError('Input must be greater than 0.')

    if n == 0:
        return 1

    return n * factorial(n-1)


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(25))