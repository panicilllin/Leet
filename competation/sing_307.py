from typing import List, Optional


class Solution1:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int,
                         energy: List[int], experience: List[int]) -> int:
        need_exp = 0
        need_ene = initialEnergy
        total_match = len(energy)

        for i in range(total_match):
            need_ene = need_ene - energy[i]
            if initialExperience - experience[i] <= 0:
                need_exp = need_exp + (experience[i] + 1 - initialExperience)
                initialExperience = experience[i] + 1

            initialExperience = initialExperience + experience[i]
        print(need_ene, need_exp)
        if need_ene > 1:
            need_ene = 0
        else:
            need_ene = 1 - need_ene
        print(need_ene, need_exp)

        return need_ene + need_exp


class Solution2:
    def largestPalindromic(self, num: str) -> str:
        if num == '':
            return ''
        num_map = {i: 0 for i in range(9, -1, -1)}
        # print(num_map)
        for n in num:
            n = int(n)
            num_map[n] += 1
        # print(num_map)
        max_mid = None
        res_stack = []
        for k, v in num_map.items():
            if v % 2 != 0 and max_mid is None:
                max_mid = k
            if v >= 2:
                res_stack.extend([k] * (v // 2))
        print(max_mid, res_stack)
        while res_stack and res_stack[0] == 0:
            res_stack.pop(0)
        res = ''
        for i in res_stack:
            res += str(i)
        if max_mid != None:
            res += str(max_mid)
        for i in res_stack[::-1]:
            res += str(i)
        if res == '':
            return '0'
        return res


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution3_dead:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if root.val == start:
            return self.tree_deep(root, 0)
        root_deep = self.tree_deep(root, 0)
        start_node, root_start = self.find_start(root, start, 0)
        start_deep = self.tree_deep(start_node, 0)
        print(root_deep, root_start, start_deep)
        if root_deep == root_start + start_deep:
            if root_start > start_deep:
                res = root_deep
            else:
                pass
        else:
            res = root_deep + root_start
        return res

    def find_start(self, root, start_val, level):
        if root.val == start_val:
            return root, level
        if root.left != None:
            left_search, left_level = self.find_start(root.left, start_val, level + 1)
            if left_search != None:
                return left_search, left_level
        if root.right != None:
            right_search, right_level = self.find_start(root.right, start_val, level + 1)
            if right_search != None:
                return right_search, right_level
        return None, None

    def tree_deep(self, root, level):
        if root is None:
            return level
        left_level = right_level = level
        if root.left != None:
            left_level = self.tree_deep(root.left, level + 1)
        if root.right != None:
            right_level = self.tree_deep(root.right, level + 1)

        return max(left_level, right_level)

    class Solution3_v2:
        def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
            while True:
                self.infact(root, start)

        def infect(self, root, start_val):
            if root is None:
                return
            if root.val != start_val:

                # chiled infected
                if (root.left and root.left.val == start_val) \
                        or (root.right and root.right.val == start_val):
                    root.val == start_val
                    return True

                # clean,continue
                else:
                    self.infect(root.left)
                    self.infect(root.right)

            else:  # infected node

                # no child node:
                if root.left is None and root.right is None:
                    return False
                # child node already infected
                if (root.left and root.left.val == start_val) \
                        and (root.right and root.right.val == start_val):
                    self.infect(root.left)
                    self.infect(root.right)

                # infect child
                if root.left and root.left.val != start_val:
                    root.left.val == start_val
                if root.right and root.right.val != start_val:
                    root.right.val == start_val
                return True

    class Solution3:
        nodes_map = {}
        start_node = None

        def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
            def dfs_tree(self, node, father_node):
                if node == None:
                    return
                if father_node:
                    self.nodes_map[node.val] = father_node
                if node.val == start:
                    self.start_node = node
                self.nodes_map(node.left, node)
                self.nodes_map(node.right, node)

            dfs_tree(root, None)
            ans = -1
            while 



if __name__ == "__main__":
    a = Solution()
    # b = a.minNumberOfHours(initialEnergy=1, initialExperience=1,
    #                        energy=[1, 1, 1, 1], experience=[1, 1, 1,50])
    b = a.v("1234432133234")
    print(b)
