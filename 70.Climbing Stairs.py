'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        result = [0] * n
        result[0] = 1
        result[1] = 2

        for i in range(2, n):
            result[i] = result[i - 1] + result[i - 2]

        print(result)
        return result[n - 1]

if __name__ == '__main__':
    s = Solution()
    s.climbStairs(3)



'''
Approach 3: Dynamic Programming
Algorithm

As we can see this problem can be broken into subproblems, and it contains the optimal substructure property i.e. its optimal solution can be constructed efficiently from optimal solutions of its subproblems, we can use dynamic programming to solve this problem.

One can reach i^{th}i 
th
  step in one of the two ways:

Taking a single step from (i-1)^{th}(i−1) 
th
  step.

Taking a step of 22 from (i-2)^{th}(i−2) 
th
  step.

So, the total number of ways to reach i^{th}i 
th
  is equal to sum of ways of reaching (i-1)^{th}(i−1) 
th
  step and ways of reaching (i-2)^{th}(i−2) 
th
  step.

Let dp[i]dp[i] denotes the number of ways to reach on i^{th}i 
th
  step:

dp[i]=dp[i-1]+dp[i-2]
dp[i]=dp[i−1]+dp[i−2]'''