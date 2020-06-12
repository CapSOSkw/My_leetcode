# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## 使用DFS, 输出所有路径.

class Solution(object):
    def DFS_Path(self, root):
        """
        :type root: TreeNode
        :rtype: paths
        """
        if not root: return False

        all_path = []

        def dfs(node, path=[]):
            if not node:
                return path

            if not node.left and not node.right:
                all_path.append(path)

            if node.left:
                dfs(node.left, path + [node.left.val])

            if node.right:
                dfs(node.right, path + [node.right.val])

        dfs(root, [root.val])

        return all_path


    def BFS_path(self, root):
        '''

        :param root: TreeNode
        :return:
        '''

        queue = [root]
        path = []

        while queue:
            node = queue.pop(0)
            path.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return path


