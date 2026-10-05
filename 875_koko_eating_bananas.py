from bisect import bisect_left
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        if h < len(piles):
            return 0
        if h > piles[-1]*len(piles):
            return 1
        k = 1+piles[-1]//2

        min_speed = 1
        max_speed = piles[-1]
        while True:
            print(f"k=={k}")
            t = 0
            for pile in piles:
                t += (pile+k-1)//k
                if t > h:
                    min_speed = max(k, min_speed)
                    continue
            print(f"t=={t}")
            if t <= h:
                max_speed = min(k, max_speed)
                if max_speed - min_speed <= 1:
                    return k
                k = (min_speed + max_speed) // 2
                print(f"k2=={k},min={min_speed},max={max_speed}")
                continue

            else:
                k = (min_speed + max_speed) // 2
                print(f"k3=={k},min={min_speed},max={max_speed}")
                if max_speed - min_speed <= 1:
                    return k+1
                continue

        # return bisect_left(range(max(piles)), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))

if __name__ =="__main__":
    a = Solution()
    b = a.minEatingSpeed(piles = [312884470], h = 968709470)
    print(b)