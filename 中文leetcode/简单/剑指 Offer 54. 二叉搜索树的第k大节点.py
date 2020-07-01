'''

给定一棵二叉搜索树，请找出其中第k大的节点。


示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数
'''


'''
解题思路：
本文解法基于此性质：二叉搜索树的中序遍历为 递增序列 。

根据以上性质，易得二叉搜索树的 中序遍历倒序 为 递减序列 。
因此，求 “二叉搜索树第 k 大的节点” 可转化为求 “此树的中序遍历倒序的第 k 个节点”。

# 打印中序遍历
def dfs(root):
    if not root: return
    dfs(root.left)  # 左
    print(root.val) # 根
    dfs(root.right) # 右



# 打印中序遍历倒序
def dfs(root):
    if not root: return
    dfs(root.right) # 右
    print(root.val) # 根
    dfs(root.left)  # 左

为求第 kk 个节点，需要实现以下 三项工作 ：
递归遍历时计数，统计当前节点的序号；
递归到第 kk 个节点时，应记录结果 resres ；
记录结果后，后续的遍历即失去意义，应提前终止（即返回）。

递归解析：
终止条件： 当节点 root 为空（越过叶节点），则直接返回；
递归右子树： 即 dfs(root.right) ；
三项工作：
提前返回： 若 k = 0 ，代表已找到目标节点，无需继续遍历，因此直接返回；
统计序号： 执行 k = k - 1（即从 k 减至 0 ）；
记录结果： 若 k = 0，代表当前节点为第 k 大的节点，因此记录 res = root.val ；
递归左子树： 即 dfs(root.left) ；

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        def dfs(root):
            if not root: return
            dfs(root.right)

            if self.k == 0: return

            self.k -= 1

            if self.k == 0: self.ans = root.val

            dfs(root.left)

        self.k = k
        dfs(root)
        return self.ans


