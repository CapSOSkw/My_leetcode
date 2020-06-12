'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

'''
100, 1000, 1000, ... n % 10 == 0
10: 1^2 + 3 ^2 = 10 -> 1^2 + 0^2 = 1
100: (6, 8)
1000: (1, 3)

'''


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = []
        num = n

        while num not in seen:
            if num == 1:
                return True

            else:
                seen.append(num)
                num = sum([int(i) ** 2 for i in str(num)])

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(11))