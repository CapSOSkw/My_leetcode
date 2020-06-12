'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:ytr
[
         [1],  #0
        [1,1],  #1
       [1,2,1],  #2
      [1,3,3,1],  #3
     [1,4,6,4,1]   #4
    [1,5,10,10,5,1]  #5
   [1,6,15,20,15,6,1]  #6
]


'''


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        else:
            result = [[1], [1, 1]]

            for i in range(2, numRows):
                lastLine = result[-1]

                subLine = []
                for i in range(len(lastLine) - 1):
                    subLine.append(lastLine[i] + lastLine[i+1])

                subLine = [1] + subLine + [1]

                result.append(subLine)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))




