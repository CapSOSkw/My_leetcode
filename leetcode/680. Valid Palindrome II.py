'''
Given a non-empty string s,
you may delete at most one character.
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.
'''

from collections import Counter, defaultdict

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == s[::-1]: return True

        b = s[::-1]

        for i in range(len(s)):
            if s[i] != b[i]:
                temp = s[:i] + s[i+1:]
                temp1 = b[:i] + b[i+1:]

                return temp == temp[::-1] or temp1 == temp1[::-1]



s = Solution()
x = 'acbba'
print(s.validPalindrome(x))

