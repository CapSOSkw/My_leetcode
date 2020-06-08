'''
给你两个整数数组 nums 和 index。你需要按照以下规则创建目标数组：

目标数组 target 最初为空。
按从左到右的顺序依次读取 nums[i] 和 index[i]，在 target 数组中的下标 index[i] 处插入值 nums[i] 。
重复上一步，直到在 nums 和 index 中都没有要读取的元素。
请你返回目标数组。

题目保证数字插入位置总是存在。


示例 1：

输入：nums = [0,1,2,3,4], index = [0,1,2,2,1]
输出：[0,4,1,3,2]
解释：
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
示例 2：

输入：nums = [1,2,3,4,0], index = [0,1,2,3,0]
输出：[0,1,2,3,4]
解释：
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
示例 3：

输入：nums = [1], index = [0]
输出：[1]
 

提示：

1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i
'''


'''
思路：
一、算法思路
（一）直接法
1 创建空的目标数组target。
2 从左到右顺序遍历数组nums和index,按照数组index中的值，将nums中的数插入到target中指定位置。
（二）不创建新数组的原地解法
顺序遍历index，如果index中的数值k等于其下标值j，说明nums中数值在合适位置无需调整。
反之，说明nums中数值nums[j]需要放到nums中下标为k的位置，
下标为k至j-1的元素后移一位。为此，用变量temp记录nums[j],逆序遍历nums[j]到nums[k+1],
将相关元素赋值为其前一个元素的值，最后将nums[k]赋值为temp。

'''

class Solution:
    def createTargetArray(self, nums, index):
        # # method1
        # N = len(nums)
        # target = []
        # for i in range(N):
        #     target.insert(index[i], nums[i])
        # return target

        # method2
        N = len(nums)
        for i in range(N):
            k = index[i]
            if k != i:
                temp = nums[i]
                # nums[k+1:i+1] = nums[k:i]
                for j in range(i, k, -1):
                    nums[j] = nums[j-1]
                nums[k] = temp
        return nums


nums = [0,1,2,3,4]
index = [0,1,2,2,1]

print(Solution().createTargetArray(nums, index))