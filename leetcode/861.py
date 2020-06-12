'''
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column,
and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves,
every row of this matrix is interpreted as a binary number,
and the score of the matrix is the sum of these numbers.

Return the highest possible score.



Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39


Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.

'''

import numpy as np
from collections import Counter

class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        A = np.array(A)
        nrows, ncols = A.shape

        # toggle first col
        first_col = A[:, 0]
        for idx, val in enumerate(first_col):
            if val == 0:
                A[idx, :] = np.array(list(map(lambda x: 1-x, A[idx, :])))


        for col in range(1, ncols):
            if sum(A[:, col]) < nrows / 2:
                A[:, col] = np.array(list(map(lambda x: 1-x, A[:, col])))


        print(A)
        # calculate score
        score = 0

        for row in A:
            num = 0
            for v in row:
                num = num << 1
                num += v
            score += num

        print(score)

S = Solution()
x = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]

# x = [[0], [1]]
S.matrixScore(x)



