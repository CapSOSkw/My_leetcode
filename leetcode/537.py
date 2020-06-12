'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi,
where the integer a and b will both belong to the range of [-100, 100].
And the output should be also in this form.
'''

import re
class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        nums_a = tuple(map(int, re.findall(r'\-?\d+', a)))
        nums_b = tuple(map(int, re.findall(r'\-?\d+', b)))

        x1, y1 = nums_a
        x2, y2 = nums_b

        real_num = x1*x2 - y1*y2
        complex_num = x1*y2 + x2*y1

        result = f'{real_num}+{complex_num}i'

        return result


s = Solution()
a, b = "1+1i", "1+1i"

print(s.complexNumberMultiply(a, b))