# @Time    : 2021/5/1 9:55
# @Author  : yhx52385
# @Email   : yhx52385@163.com
# @File    : 142-linked-list-cycle-ii.py
# @software: PyCharm
# Definition for singly-linked list.

# already finished in company
# 快慢指针(best)or哈希表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        return