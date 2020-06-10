'''
实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。

 

示例：

输入：单向链表a->b->c->d->e->f中的节点c
结果：不返回任何数据，但该链表变为a->b->d->e->f

'''

'''
思路：

这题的核心思想其实就是把node的下一位的值覆盖给node，然后跳过node的下一位
因为我们无法访问到head节点，所以除了直接从node开始往下找，其他都是不现实的
即
a->b->c->d->e->f 变为 a->b->d->d->e->f 然后把第一个d的next设为e，跳过第二个d

'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next