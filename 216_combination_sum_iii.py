from typing import *


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        viliagers = []
        lawers = {}
        for i in trust:
            sub = i[0]
            obj = i[1]
            if sub not in viliagers:
                viliagers.append(sub)
            if obj not in lawers:
                lawers[obj] = [sub]
            else:
                lawers[obj].append(sub)
                lawers[obj].sort()
        viliagers.sort()
        print(viliagers)
        print(lawers)
        if len(viliagers) != n-1:
            return -1
        for i in lawers:
            if lawers[i] == viliagers:
                return i
        return -1


if __name__ == "__main__":
    a = Solution()
    b = a.findJudge(n=4, trust=[[3,2],[4,1],[3,1],[2,1],[2,3],[4,3],[4,2],[3,4]])
    print(b)
