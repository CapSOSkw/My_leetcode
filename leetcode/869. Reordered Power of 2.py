'''
Starting with a positive integer N, we reorder the digits in any order
(including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true

Example 2:

Input: 10
Output: false

Example 3:

Input: 16
Output: true

Example 4:

Input: 24
Output: false

Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9
'''

import collections
class Solution(object):
    def reorderedPowerOf2(self, N):
        count = collections.Counter(str(N))
        x = [collections.Counter(str(1 << b)) for b in range(31)]
        print(x)

        return any(count == collections.Counter(str(1 << b))
                   for b in range(31))

s = Solution()
n = 46

print(s.reorderedPowerOf2(n))