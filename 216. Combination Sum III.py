'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique
set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def dfs(k, n, ans, res, start):
            if k == 1:
                if n > ans[-1] and n < 10:
                    ans += [n]
                    res.append(ans)
                    return
            for i in range(start, 9):
                if n < start: break
                dfs(k-1, n-i, ans+[i], res, i+1)
            return res


        result = dfs(k, n, [], [], 1)
        return result

s = Solution()

k = 2
n = 5

print(s.combinationSum3(k, n))




















































