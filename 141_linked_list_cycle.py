from typing import Optional


# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_nd = head
        slow_nd = head
        while fast_nd is not None and fast_nd.next is not None:
            fast_nd = fast_nd.next.next
            slow_nd = slow_nd.next
            if fast_nd == slow_nd:
                return True
        return False

# AC
