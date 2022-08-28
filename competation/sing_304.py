import copy
from typing import List


class Solution1:
    def minimumOperations(self, nums: List[int]) -> int:

        res = 0
        while sum(nums) > 0:
            nums.sort()
            x = None
            i = 0
            while i < len(nums):
                if nums[i] <= 0:
                    i += 1
                    continue
                else:
                    x = nums[i]
                    break
            nums = nums[i + 1:]
            nums = [j - x for j in nums]
            res += 1
        return res


class Solution2:
    def maximumGroups(self, grades: List[int]) -> int:
        if len(grades) <= 2:
            return 1
        grades.sort()
        print(grades)
        groups = []
        i = 1
        needle = 0
        new_grades = copy.deepcopy(grades)
        while i < len(grades) and new_grades:
            new_group = new_grades[:i]
            new_grades = new_grades[i:]
            i += 1
            needle += i
            print(new_group)
            groups.append(new_group)

        print(groups)
        if len(groups[-1]) <= len(groups[-2]) or sum(groups[-1]) <= sum(groups[-2]):
            return len(groups) - 1
        return len(groups)


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        loop1, walk1 = self.checkloop(edges, node1)
        loop2, walk2 = self.checkloop(edges, node2)
        if loop1 is True or loop2 is True:
            # one of the node in loop
            if loop1 is True and loop2 is False:
                return -1
            elif loop1 is False and loop2 is True:
                return -1
            elif loop1 is True and loop2 is True:
                return self.find_minium_node(edges, node1, node2, None)
            else:
                if loop1 is True:
                    return self.find_minium_node(edges, node1, node2, loop2)
                else:
                    return self.find_minium_node(edges, node1, node2, loop1)
        # print(f"loop1={loop1},loop2={loop2}")
        if loop1 is False and loop2 is False:
            # noloop
            return self.find_combine(edges, node1, node2)
        elif loop1 and loop2:
            # bothloop
            if loop1 == loop2:
                # what if node1 or node2 before loop
                if walk1 > walk2:
                    return node2
                elif walk2 > walk1:
                    return node1
                else:
                    return min(node1, node2)
                # return self.find_minium_node(edges,node1,node2,loop1)
            else:
                return self.find_combine_loop(edges, loop1, loop2, walk1, walk2)
        else:
            return -1

    def checkloop(self, edges, node):
        if edges[node] == -1:
            return False, None
        i = edges[edges[node]]
        j = edges[node]
        if i == -1:
            return False, None
        while i != j and edges[i] != -1 and i != node:
            i = edges[i]
            i = edges[i]
            j = edges[j]
        if edges[i] == -1:
            return False, None
        if i == node:
            return True, None
        if i != j:
            return False, None
        i = node
        move = 0
        while i != j:
            i = edges[i]
            j = edges[j]
            move += 1
        return i, move

    def find_combine(self, edges, node1, node2):
        # noloop
        # it's ok that node1 and node2 are before public_node
        i = node1
        j = node2
        move = 0
        while edges[i] != -1:
            i = edges[i]
            move += 1
        while edges[j] != -1:
            j = edges[j]
            move -= 1
        if i != j:
            return -1

        p = node1
        q = node2
        if move > 0:
            while move > 0:
                p = edges[p]
                move -= 1
        elif move < 0:
            while move < 0:
                q = edges[q]
                move += 1
        while p != q:
            p = edges[p]
            q = edges[q]
        public_node = p
        return public_node

    def find_combine_loop(self, edges, loop1, loop2, walk1, walk2):

        if_combine = False
        i = edges[loop1]
        walk1s = walk1 + 1
        while i != loop1:
            i = edges[i]
            walk1s += 1
            if i == loop2:
                if_combine = True
                walk1s += 1
                break
        if if_combine is False:
            return -1

        j = edges[loop2]
        walk2s = walk2 + 1
        while j != loop2:
            i = edges[i]
            walk1s += 1
            if j == loop1:
                walk2s += 1
                break
        # 选loop1:
        if walk2s < walk1s:
            return loop1
        else:
            return loop2

    def find_minium_node(self, edges, node1, node2, public_node=None):
        i = node1
        j = node2
        walk1 = 0
        walk2 = 0
        if not public_node:
            while i != j:
                i = edges[i]
                walk1 += 1
            while j != i:
                j = edges[j]
                walk2 += 1
        else:
            while i != public_node:
                i = edges[i]
                walk1 += 1

            while j != public_node:
                j = edges[j]
                walk2 += 1

        if walk1 > walk2:
            return node2
        elif walk2 > walk1:
            return node1
        else:
            return min(node1, node2)

    if __name__ == "__main__":
        a = Solution()
        b = a.closestMeetingNode(edges=[-1, 0], node1=1, node2=0)
        print(b)
