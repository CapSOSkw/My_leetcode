'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""

        while n > 0:
            mod = n % 26
            tmp = n // 26

            if mod == 0:
                mod = 26
                tmp -= 1

            result += chr(mod + 64)  # 26 + 64

            n = tmp

        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(27))