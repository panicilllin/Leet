from math import inf
from typing import List
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist_1 = [inf]*len(edges)
        dist_2 = [inf]*len(edges)
        min_wk = inf
        res = -1
        dist_1[node1] = 0
        dist_2[node2] = 0
        dist_1 = self.cal_walk(edges, node1, dist_1)
        dist_2 = self.cal_walk(edges, node2, dist_2)
        for i in range(len(edges)):
            wk1 = dist_1[i]
            wk2 = dist_2[i]
            if wk1 != inf and wk2 != inf:
                wk = max(wk1, wk2)
                if wk < min_wk:
                    min_wk = wk
                    res = i
        return res


    def cal_walk(self,edges,node,dist=None):
        dist = [inf]*len(edges) if not dist else dist
        i = node
        walk = 0
        while edges[i] != -1 and edges[i] != node:
            i = edges[i]
            walk += 1
            if dist[i] < walk:
                break
            dist[i] = min(dist[i], walk)
        print(dist)
        return dist



if __name__ == "__main__":
    a = Solution()
    b = a.closestMeetingNode(edges = [5,4,5,4,3,6,-1], node1 = 0, node2 = 1)
    print(b)

# AC
