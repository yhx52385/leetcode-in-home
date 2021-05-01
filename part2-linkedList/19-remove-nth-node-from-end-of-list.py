# @Time    : 2021/5/1 9:35
# @Author  : yhx52385
# @Email   : yhx52385@163.com
# @File    : 19-remove-nth-node-from-end-of-list.py
# @software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        count = 0
        now = dummy
        while(count<n and now):
            count += 1
            now = now.next

        start = dummy
        end = now
        before = None
        while(end):
            before = start
            start = start.next
            end = end.next
        if(before is not None):
            before.next = start.next
            return dummy.next
        else:
            return None
