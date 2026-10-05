from curses.ascii import SO
from typing import List
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        for i in range(k):
            if i % 2 ==0:
                res.append(i//2+1)
            else:
                res.append(n-i//2)
        print(res)
        if k % 2 == 0:
            for i in range(n-k//2,k//2,-1):
                res.append(i)
        else:
            for i in range(k//2+2,n-k//2+1):
                res.append(i)
        print(res)
        return res

if __name__ =="__main__":
    a = Solution()
    b = a.constructArray(6,4)

# AC