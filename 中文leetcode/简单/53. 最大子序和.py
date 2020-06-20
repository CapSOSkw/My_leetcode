'''

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3, 4,-1,2,1,-5, 4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

'''

class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0: return 0

        if len(nums) == 1: return nums[0]

        dp = nums[:]   # # 初始化dp数组，dp[i]存储以nums[i]为结尾的子数组的和的最大值
        res = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i]+dp[i-1])    # # 更新dp[i]
            res = max(res, dp[i])    # 更新全局最大值

        return res


print(Solution().maxSubArray([-2,1,-3, 4,-1,2,1,-5, 4]))









