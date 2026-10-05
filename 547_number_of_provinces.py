from typing import List, Optional

class UnionFind:
    def __init__(self,father={},val:int=None):
        self.father = father
        self.val = val
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
    
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        return root

    def merge(self, x, y, val):
        root_x, root_y = self.find(x)
        if root_x != root_y:
            self.father[root_x] = root_y
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    

# 并查集
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if isConnected[i][j] == 1:
                    node = UnionFind(None,i)
                    node2 = UnionFind(node,j)
                
                