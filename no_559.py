
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = []
        queue.append(root)
        level = 0
        if root is None:
            return level
        while queue:
            queueLen = len(queue)
            level += 1
            for i in range(queueLen):
                print(f"queue1==={[item.val for item in queue]},{level}")
                node = queue.pop(0)
                if node.children is not None and len(node.children)>0:
                    for j in node.children:
                        queue.append(j)
                        print(f"queue2==={[item.val for item in queue]},{level}")
        return level

    def DFS(self, root: 'Node') -> int:
        if root is None:
            return 0
        depth = 1
        for node in root.children:
            depth = max(depth, self.DFS(node)+1)
        return depth