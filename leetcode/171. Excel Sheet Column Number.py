'''

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for idx, c in enumerate(s[::-1]):
            toNum = ord(c) - 64
            result += toNum * 26 ** idx

        print(result)


if __name__ == '__main__':
    s = Solution()
    s.titleToNumber('AAA')