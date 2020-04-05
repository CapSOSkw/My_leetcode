'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

from collections import defaultdict, Counter
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = defaultdict(list)
        dt = defaultdict(list)
        for idx, c in enumerate(s):
            ds[c].append(idx)

        for idx, c in enumerate(t):
            dt[c].append(idx)

        ls = [i for i in ds.values()]
        lt = [i for i in dt.values()]

        return sorted(ls) == sorted(lt)


if __name__ == '__main__':

    s = 'paper'
    t = 'title'
    sol = Solution()
    print(sol.isIsomorphic(s, t))

