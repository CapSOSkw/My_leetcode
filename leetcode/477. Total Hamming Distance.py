'''
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
'''

from itertools import combinations
class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return sum(map(lambda x: bin(x[0]^x[1]).count('1'), combinations(nums, 2)))  # time limit exceeded

        # 对比 ith 的0， 1 数量， score =  N(0) * N(1)

        temp = zip(*map('{:032b}'.format, nums))
        print(list(map('{:032b}'.format, nums)))
        print(list(zip(*map('{:032b}'.format, nums))))

        result = sum(b.count('0') * b.count('1') for b in temp)

        return result




s = Solution()

nums = [4, 14, 2]

print(s.totalHammingDistance(nums))

