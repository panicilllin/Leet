from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_node=None
        head0 = ListNode('A', head)
        node = head0
        while node.next is not None:
            if node.val == node.next.val:
                unique_node = node
            elif unique_node != None:
                unique_node.next=node.next
                unique_node = None
            node=node.next
        if unique_node and unique_node.val == node.val:
            unique_node.next=None
        return head0.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        unique_node=None
        unique_nodes=[]
        head0=ListNode(-1,head)
        node = head0
        while node.next != None:
            if node.val == node.next.val:
                unique_node = node
                unique_nodes.append(node)
            elif unique_node != None:
                unique_node.next=node.next
                unique_node = None
            node=node.next
        if unique_node and unique_node.val == node.val:
            unique_node.next=None


        node = head0
        while node.next is not None and len(unique_nodes)!=0:
            # print(node.val, node.next.val)
            if node.next.val == unique_nodes[0].val:
                del unique_nodes[0]
                node.next=node.next.next
                # print(node.val, node.next.val)
            else:
                node = node.next

        return head0.next

if __name__ == "__main__":
    a = Solution()

    # [1, 2, 3, 3, 4, 4, 5]
    # n5 = ListNode(5, None)
    # n44 = ListNode(4, n5)
    # n4 = ListNode(4, n44)
    # n33 = ListNode(3, n4)
    # n3 = ListNode(3, n33)
    n2 = ListNode(1, None)
    n1=ListNode(1,n2)

    b = a.deleteDuplicates(n1)
    print(b)


# AC