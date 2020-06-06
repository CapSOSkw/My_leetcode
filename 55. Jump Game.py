'''
Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farest_index = nums[0]
        for i in range(1, len(nums)):
            if i > farest_index:
                return False
            if i + nums[i] > farest_index:
                farest_index = i + nums[i]
                if farest_index == len(nums)-1:
                    return True
        return True

s = Solution()

nums = [2, 3, 1, 0, 4]

print(s.canJump(nums))


