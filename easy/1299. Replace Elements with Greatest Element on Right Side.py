'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]


Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''


class Solution:
    def replaceElements(self, arr):
        max_n = arr[-1]
        result = [-1]

        for i in arr[:-1][::-1]:
            result.insert(0, max_n)
            max_n = max(i, max_n)

        return result


print(Solution().replaceElements([17,18,5,4,6,1]))