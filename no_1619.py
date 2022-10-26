from typing import List
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        cut = n//20
        arr.sort()
        return sum(arr[cut:-cut])/len(arr[cut:-cut])