'''
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to
the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
'''

from functools import reduce
from copy import copy
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        zeroNum = nums.count(0)

        for i in nums:
            if (i != 0):
                product = product * i
        if (zeroNum > 1):
            return [0 for _ in range(len(nums))]
        elif (zeroNum == 0):
            return [product // i for i in nums]
        else:
            return [product if i == 0 else 0 for i in nums]


s = Solution()
nums = [1,2,3,0]
print(s.productExceptSelf(nums))


'''
1. 如果nums中存在2个及以上数量的0， 那么乘积必然都等于0
2. 如果只存在一个0， 那除了0位置以外， 都等于零； 0位置上等于最大乘积
3. 如果不存在0， 对应位置等于最大乘积除于相应位置的数值。
'''
