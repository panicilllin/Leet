#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
# https://leetcode.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (57.56%)
# Likes:    3289
# Dislikes: 276
# Total Accepted:    153.9K
# Total Submissions: 250K
# Testcase Example:  '[1,2,3]\n5'
#
# Given the head of a singly linked list and an integer k, split the linked
# list into k consecutive linked list parts.
# 
# The length of each part should be as equal as possible: no two parts should
# have a size differing by more than one. This may lead to some parts being
# null.
# 
# The parts should be in the order of occurrence in the input list, and parts
# occurring earlier should always have a size greater than or equal to parts
# occurring later.
# 
# Return an array of the k parts.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a
# ListNode is [].
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most
# 1, and earlier parts are a larger size than the later parts.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # count len
        node_len=0
        node=head
        res = []
        while node != None:
            node=node.next
            node_len+=1
        res = []
        if node_len//k < 1:
            res = [1]*node_len+[0]*(k-node_len)
        elif node_len%k == 0:
            res = [node_len//k]*k
        else:
            res = [node_len//k+1]*(node_len%k) + [node_len//k]*(k-node_len%k)
        print(node_len,k,res)
        ans = []
        node = head
        for step in res:
            pre_head,node=self.splite_node(node,step)
            ans.append(pre_head)
        return ans
        
    def splite_node(self, head,k):
        if head is None:
            return None, None 
        node = head
        for i in range(0,k-1):
            if node == None:
                break
            node = node.next
        if node is not None:
            next_head = node.next
            node.next = None
        else:
            next_head = None
        return head, next_head



# @lc code=end

