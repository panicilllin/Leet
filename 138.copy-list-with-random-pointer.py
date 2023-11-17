
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        node = head
        if head == None:
            return
        cp_head = Node(x=node.val)
        cp_node = cp_head
        hash_map={node:cp_node,None:None}
        
        while node.next != None:
            
            cp_node = self.copy_node(node,cp_node)
            node = node.next
            hash_map[node] = cp_node
        node = head
        cp_node = cp_head
        while node != None:
            # print(node.val)
            # print(node.random.val if node.random is not None else node.random)
            # print(hash_map[node].val)
            # print(hash_map[node].random)
            # print('------')

            cp_node.random = hash_map[node.random]
            node = node.next
            cp_node = cp_node.next
        return cp_head
    
    def copy_node(self,head,copy_head):
        next_node = head.next
        copy_next = Node(x=next_node.val)
        copy_head.next = copy_next
        return copy_next
    


if __name__ =="__main__":
    a = Solution
    b = a.copyRandomList()