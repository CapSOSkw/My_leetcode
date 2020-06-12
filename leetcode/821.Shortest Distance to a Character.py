'''
Given a string S and a character C, return an array of integers
representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''
import sys
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_index = [idx for idx, n in enumerate(S) if n == C]
        # print(c_index)
        pop_index = [(c_index[i] + c_index[i+1]) // 2 for i in range(len(c_index) - 1)] + [len(S)]
        # print(pop_index)

        result = []
        for i in range(len(S)):
            result.append(abs(i - c_index[0]))
            if i == pop_index[0]:
                c_index.pop(0)
                pop_index.pop(0)
        print(result)
        return result

if __name__ == '__main__':
    S = 'loveleetcode'
    C = 'e'
    s = Solution()
    s.shortestToChar(S, C)
