'''
Given a positive integer n, break it into the sum of at least two positive integers and
maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''


'''
1.   1
2.   1+1
3.   2+1
4.   2+2
5.   3+2
6.   3+3
7.   3+2+2
8.   3+3+2
9.   3+3+3
10.  3+3+2+2
11.  3+3+3+2
12.  3+3+3+3
13.  3+3+3+2+2
14.  3+3+3+3+2
15.  3+3+3+3+3
16.  3+3+3+3+2+2
17.  3+3+3+3+3+2
18.  3+3+3+3+3+3
...

'''
from functools import reduce
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        def f(n):
            if n % 3 == 0:
                return [3] * int((n / 3))

            else:
                q = n // 3

                if n - 3 * q < 2:
                    q -= 1

                return [3] * q + [n - 3 * q]

        if n < 3: return 1
        if n == 3: return 2
        return int(reduce(lambda x, y: x*y, f(n)))


def f(n):
    if n % 3 == 0:
        return [3] * int((n / 3))

    else:
        q = n // 3

        if n - 3*q < 2:
            q -= 1

        return [3] * q + [n - 3*q]

print(f(17))


s = Solution()


# print(s.integerBreak(3))




