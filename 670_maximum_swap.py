import copy
from os import lstat
from tkinter import N

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_l = [int(i) for i in str(num)]
        print(num_l)
        n = len(num_l)
        res = 0
        idx= [None for i in range(n)]
        j = 0
        for i in range(n):
            if num_l[i] > num_l[j]:
                j = i
            idx[i] = j
        
            
if __name__ == "__main__":
    a = Solution()
    b = a.maximumSwap(7736)
    print(b)