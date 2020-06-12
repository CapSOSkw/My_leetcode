'''
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''

from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}

        for i in range(len(nums)):
            if str(nums[i]) not in dic.keys():
                dic[str(nums[i])] = {'cur': i}
            else:

                diff = i - dic[str(nums[i])]['cur']
                if diff <= k:
                    return True
                else:
                    dic[str(nums[i])] = {'diff': diff}
                    dic[str(nums[i])]['cur'] = i

        return False

s = Solution()
nums = [1,2,3,1,2,3]
k = 1

print(s.containsNearbyDuplicate(nums, k))
