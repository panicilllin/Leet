from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i=0
        while i < len(arr):
            flg=False
            for key in pieces:
                if arr[i:i+len(key)] == key:
                    i+=len(key)
                    flg=True
                    break
            if flg is False:
                return False
                    
                
        return True