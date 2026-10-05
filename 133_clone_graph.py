'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

'''
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import defaultdict, deque
class Solution1:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        graph = defaultdict(dict)
        queue = deque([node])
        res = defaultdict(dict)
        while queue:
            curr_node = queue.popleft()
            if not graph.get(curr_node.val):
                graph[curr_node.val] = Node(curr_node.val, [n.val for n in curr_node.neighbors]) # type: ignore
            for neighbor in curr_node.neighbors:
                if not graph.get(neighbor.val):
                    queue.append(neighbor)

        for idx, n in graph.items():
            neighbor_nodes = []
            for neighbor_val in n.neighbors: # type: ignore
                neighbor_nodes.append(graph[neighbor_val])
            n.neighbors=neighbor_nodes # type: ignore
        
        return graph.get(node.val) # type: ignore


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        graph = {}
        graph[node] = Node(node.val)
        queue = deque([node])
        while queue:
            curr_node = queue.popleft()
            # graph[curr_node] = Node(curr_node.val)
            for neighbor in curr_node.neighbors:
                if not graph.get(neighbor):
                    graph[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                graph[curr_node].neighbors.append(graph[neighbor])
        return graph.get(node)
            
        

if __name__ == '__main__':
    s = Solution()
    node = Node(1, [Node(2), Node(3)])
    node.neighbors[0].neighbors = [Node(4)]
    node.neighbors[1].neighbors = [Node(5)]
    cloned_node = s.cloneGraph(node)
    print(f"node {node} ==> {node.val}; cloned_node {cloned_node} ==> {cloned_node.val}") # type: ignore
    print(f"node.neighbors {node.neighbors}")
    print(f"cloned_node.neighbors {cloned_node.neighbors}") # type: ignore
