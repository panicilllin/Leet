# Definition for a binary tree node.
from collections import defaultdict
from sortedcontainers import SortedSet

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.tree = SortedSet()
        self.tree.add((0, root))
        n = 0
        self.tree_to_list(root, n)
        print(self.tree)

    def tree_to_list(self, root: TreeNode, n):
        # print(root.left, root.right,n)
        if root.right is not None:
            # self.tree[2 * n + 2] = root.right.val
            self.tree.add((2 * n + 2, root.right))
            self.tree_to_list(root.right, n=2 * n + 2)
        if root.left is not None:
            # self.tree[2 * n + 1] = root.left.val
            self.tree.add((2 * n + 1, root.left))
            self.tree_to_list(root.left, 2 * n + 1)

    def insert(self, val: int) -> int:
        last_index = len(self.tree)
        new_tree = TreeNode(val=val)
        father_index = int((last_index-1)/2)
        father_tree = self.tree[father_index][1]
        if father_tree.left is not None:
            father_tree.right = new_tree
        else:
            father_tree.left = new_tree
        # print(father_index,father_tree[1].val)
        self.tree.add((last_index, new_tree))
        return father_tree.val

    def get_root(self) -> TreeNode:
        return self.tree[0][1]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()


if __name__ == "__main__":
    node4 = TreeNode(4, None, None)
    node3 = TreeNode(3, None, None)
    node2 = TreeNode(2, node4, None)
    node1 = TreeNode(1, None, None)
    a = CBTInserter(root=node1)
    a.insert(2)
    # a.insert(6)
    print(a.get_root())

