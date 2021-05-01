# @Time    : 2021/5/1 9:18
# @Author  : yhx52385
# @Email   : yhx52385@163.com
# @File    : 206-reverse-linked-list.py
# @software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        now = dummy.next
        before = None
        while(now):
            next = now.next
            now.next = before
            before = now
            now = next
        return before



