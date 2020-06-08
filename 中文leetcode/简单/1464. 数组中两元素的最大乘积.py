'''

给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。

请你计算并返回该式的最大值。

 

示例 1：

输入：nums = [3,4,5,2]
输出：12
解释：如果选择下标 i=1 和 j=2（下标从 0 开始），
则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12 。
示例 2：

输入：nums = [1,5,4,5]
输出：16
解释：选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。
示例 3：

输入：nums = [3,7]
输出：12
 

提示：

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

'''

'''
思路：找到最大值及第二最大值（两者可以相等）

1。 遍历 O（n）
2。 排序，最低的复杂度也是O（n）
'''

class Solution:
    def maxProduct(self, nums) -> int:

        max_val = nums[0]
        second_max_val = float('-inf')

        for i in nums[1:]:
            if i >= max_val:
                max_val, second_max_val = i, max_val

            elif second_max_val <=i< max_val:
                second_max_val = i

            else:
                continue

        return (max_val-1)*(second_max_val-1)


