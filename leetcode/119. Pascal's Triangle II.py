'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        if rowIndex == 2:
            return [1, 2, 1]

        else:
            start = [1, 2, 1]

            while start[1] < rowIndex:
                newLine = [1] + [start[i]+start[i+1] for i in range(len(start) - 1)] + [1]

                start = newLine

            return start

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(7))
