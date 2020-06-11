'''
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。

 

示例 1：

输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
示例 2：

输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
输出：23
 

提示：

树中的结点数量最多为 10000 个。
最终的答案保证小于 2^31。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
思路：
当前节点为 null 时返回 0
当前节点 X < L 时则返回右子树之和
当前节点 X > R 时则返回左子树之和
当前节点 X >= L 且 X <= R 时则返回：当前节点值 + 左子树之和 + 右子树之和


'''

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def dfs(node):
            if L<=node.val<=R:
                self.ans += node.val

            if node.val < L:
                dfs(node.left)

            if node.val < R:
                dfs(node.right)


        self.ans = 0
        dfs(root)

        return self.ans


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        ans = 0
        stack = [root]

        while stack:
            node = stack.pop()

            if L<=node.val<=R:
                ans += node.val

            if node.val > L:
                stack.append(node.left)

            if node.val < R:
                stack.append(node.right)

        return ans


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        if not root: return 0

        if root.val < L:
            return self.rangeSumBST(root.right, L, R)

        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return root.val + self.rangeSumBST(root.left, L, R)+self.rangeSumBST(root.right, L, R)
