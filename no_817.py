
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        res=0
        node = head
        start_node=None
        while node != None:
            # print(node.val)
            if start_node == None and node.val in nums:
                start_node = node
                node=node.next
                res += 1
            elif node.val in nums:
                node=node.next
            else:
                start_node = None
                node = node.next
        return res

if __name__ == '__main__':
    a = Solution()
    # n4 = ListNode(4,None)
    n3 = ListNode(3,None)  
    n2 = ListNode(2,n3) 
    n1 = ListNode(1,n2) 
    n0 = ListNode(0,n1) 
    b = a.numComponents(head = n0, nums = [0,1,3])
    print(b)

#AC