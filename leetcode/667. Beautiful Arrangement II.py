'''
Given two integers n and k, you need to construct a list which contains n different positive integers ranging
from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|]
has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1]
has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1]
has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104.
'''

class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        a = [i for i in range(1, n + 1)]
        for i in range(1, k):
            a[i:] = a[:i - 1:-1]
        return a



'''
Start with the numbers sorted, e.g., 1 2 3 4 5 6 7 8 9 10. 
Then we only have difference 1, many times. 
We can create the largest possible difference by making the smallest and largest number neighbors. 
In the example, let's bring 10 next to 1. If we do this by reversing the whole subarray from 2 to 10, 
then no other neighborships in 2 to 10 are affected: 1 10 9 8 7 6 5 4 3 2. 
To create the next larger possible difference, 
we can bring 2 next to 10 by reversing the subarray from 9 to 2: 1 10 2 3 4 5 6 7 8 9. 
And so on, reversing shorter and shorter suffixes. Just create as many differences as requested.

Python

def constructArray(self, n, k):
    a = range(1, n+1)
    for i in range(1, k):
        a[i:] = a[:i-1:-1]
    return a
    
'''


s = Solution()

n = 10
k = 6

print(s.constructArray(n, k))