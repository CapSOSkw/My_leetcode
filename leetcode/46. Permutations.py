'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

from itertools import permutations

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return [list(i) for i in permutations(nums)]

        if len(nums) == 1:
            return [nums]
        else:
            to_return = []
            for i, x in enumerate(nums):
                for sub_result in self.permute(nums[:i] + nums[i+1:]):
                    to_return.append([x] + sub_result)
            return to_return




nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))