'''
Given a circular array (the next element of the last element is the
first element of the array),
print the Next Greater Number for every element.
The Next Greater Number of a number x is the first greater number
to its traversing-order next in the array, which means you could
search circularly to find its next greater number.
If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly,
which is also 2.
Note: The length of given array won't exceed 10000.
'''


class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, res, n = [], [-1]*len(nums), len(nums)
        for i in range(0, 2*n):

            while stack and nums[i % n] > nums[stack[-1]]:
                x = nums[i % n]
                y = nums[stack[-1]]
                top = stack.pop()
                if res[top] == -1:
                    res[top] = nums[i%n]
            stack.append(i % n)
        return res


s = Solution()

nums = [1, 3, 2, 5, 7, 6]

print(s.nextGreaterElements(nums))