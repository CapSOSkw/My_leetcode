'''
Given an array of numbers nums, in which exactly two elements appear only once and
'all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        last_idx = {n: idx for idx, n in enumerate(nums)}   # get the last index of each number

        res = []
        for k, v in last_idx.items():

            if nums.index(k) == v:  # if the first index of number equals to the last index, then append to the result
                res.append(k)

        return res

        # return [n for n, v in Counter(nums).items() if v == 1]
s = Solution()

x = [1,2,1,3,2,5]

print(s.singleNumber(x))