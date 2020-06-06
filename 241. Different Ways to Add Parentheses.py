'''
Given a string of numbers and operators, return all possible results
from computing all the different possible ways to group numbers and operators.
The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
( 2 * (3- (4*5) ) ) = -34
( (2*3) - (4*5) ) = -14
( ( 2 * (3-4) ) *5 ) = -10
( 2 * ( (3-4) * 5) ) = -10
( ( (2*3) - 4 ) *5 ) = 10
'''


# 符号都存在奇数位， (1, 3, 5, 7, ...)
# 按符号的位置递归
import re, operator
class Solution:


    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        tokens = re.split('(\D)', input)
        nums = list(map(int, tokens[::2]))
        ops = list(map({'+': operator.add, '-': operator.sub,
                        '*': operator.mul}.get, tokens[1::2]))

        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a, b)
                    for i in range(lo, hi)
                    for a in build(lo, i)
                    for b in build(i + 1, hi)]

        return build(0, len(nums) - 1)

i = '2*3-4*5'
s = Solution()
print(s.diffWaysToCompute(i))
