# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head.next is None:
            return True
        node_stack = [head.val]
        fast_node=head
        slow_node=head
        while  fast_node.next is not None and fast_node.next.next is not None:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            node_stack.append(slow_node.val)
        while slow_node.next is not None:
            last_val = node_stack.pop()
            slow_node = slow_node.next
            if slow_node.val != last_val:
                return False
        return True


class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        val_list=[head.val]
        while head.next:
            head=head.next
            val_list.append(head.val)

        while len(val_list)>1:
            st=val_list.pop(0)
            ed=val_list.pop(-1)
            if st != ed:
                return False
