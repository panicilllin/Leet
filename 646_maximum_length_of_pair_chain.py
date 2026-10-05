from typing import List

class Solution1:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: (x[1]))
        print(pairs)
        pair_dict = {}
        for i, pair in enumerate(pairs):
            pair_dict = self.pair(i,pair,pair_dict)
        
        print(pair_dict)
        res = 0
        for val in pair_dict.values():
            res = max(res, val[2])
        return res
        
    
    def pair(self,idx, pair,pair_dict):
        should_new=True
        for key, val in pair_dict.items():
            if val[1] < pair[0]:
                pair_dict[key][1] = pair[1]
                pair_dict[key][2] += 1
                should_new = False
        if should_new:
            pair_dict[idx] = [pair[0],pair[1],1]
        
        return pair_dict
    
    
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: (x[0],x[1]))
        print(pairs)
        pair_dict = {}
        pass 
 
if __name__ == "__main__":
    a = Solution()
    b = a.findLongestChain([[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]])
    print(b)