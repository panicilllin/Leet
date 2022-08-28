from math import inf
from typing import List


class Solution0:
    def longestCycle(self, edges: List[int]) -> int:
        node = 0
        dist = [inf] * len(edges)
        dist[node] = 0
        dist, in_node, loop_size = self.cal_walk(edges, node, dist)
        print(dist, in_node, loop_size)
        loops = {}
        in_nodes = []
        res = -1
        if in_node != None:
            loops[in_node] = loop_size
            in_nodes.append(in_node)
            res = loop_size
        for i in range(len(edges)):
            if dist[i] == inf:
                # 没走过的节点
                # dist2, in_node2, loop_size2 = self.cal_walk(edges, node)
                # print(dist2, in_node2, loop_size2)
                in_node, loop_size = self.checkloop(edges, i, in_nodes)
                if in_node:
                    print(in_node, loop_size)
                    in_nodes.append(in_node)
                    loops[in_node] = loop_size
                    res = max(res, loop_size)
        print(loops)
        return res

    def checkloop(self, edges, node, in_nodes=None):
        if edges[node] == -1:
            return False, None
        i = edges[edges[node]]
        j = edges[node]
        if i == -1:
            return False, None
        while i != j and edges[i] != -1:
            i = edges[i]
            i = edges[i]
            j = edges[j]
        if edges[i] == -1:
            return False, None
        i = node
        move = 0
        while i != j:
            i = edges[i]
            j = edges[j]
            move += 1
        walk = 1
        j = i
        while edges[j] != i:
            j = edges[j]
            walk += 1
        return i, walk

    def cal_walk(self, edges, node, dist=None):
        dist = [inf] * len(edges) if not dist else dist
        i = node
        walk = 0
        while edges[i] != -1 and edges[i] != node:
            i = edges[i]
            walk += 1
            if dist[i] < walk and dist[i] != inf:
                # print('FlgA')
                dist[i] = True
                return dist, i, walk - 1
            dist[i] = min(dist[i], walk)
        if edges[i] == node:
            # print('FlgB')
            dist[node] = True
            return dist, i, walk + 1
        return dist, None, None

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        time = [0] * len(edges)
        clock, ans = 1, -1
        print(time)
        for x, t in enumerate(time):
            print(x,t)
            if t: continue
            start_time = clock
            while x >= 0:
                if time[x]:  # 重复访问
                    if time[x] >= start_time:  # 找到了一个新的环
                        ans = max(ans, clock - time[x])
                    break
                time[x] = clock
                clock += 1
                x = edges[x]
        print(time)
        return ans


if __name__ == "__main__":
    a = Solution()
    b = a.longestCycle(edges=[5, 8, -1, 5, -1, 6, 1, 6, 6, 5])
    print(b)
