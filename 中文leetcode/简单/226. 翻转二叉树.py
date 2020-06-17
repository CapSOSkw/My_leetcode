'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''

'''
思路：
终止条件：当前节点为null时返回
交换当前节点的左右节点，再递归的交换当前节点的左节点，递归的交换当前节点的右节点
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root