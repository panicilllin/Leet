from typing import List
import heapq
from collections import defaultdict


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        all_list= {}
        for i in position:
            if not all_list.get(i):
                all_list[i] = 1
            else:
                all_list[i] = all_list[i] + 1

        left_list = 0
        right_list = 0
        for k in all_list:
            if k%2==0:
                left_list+=all_list[k]
            else:
                right_list+=all_list[k]
        return min(left_list,right_list)



if __name__ == "__main__":
    a = Solution()
    b = a.minCostToMoveChips(position=[2,2,2,3,3])
    print(b)
    # passed
