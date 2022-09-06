from typing import List, Optional

class UnionFind:
    def __init__(self,father=None,val:int=None):
        self.father = father
        self.val = val


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if isConnected[i][j] == 1:
                    node = UnionFind(None,i)
                    node2 = UnionFind(node,j)
                
                