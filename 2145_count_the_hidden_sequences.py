from typing import *


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_num = 0
        max_num = 0
        st_num = 0
        for diff in differences:
            st_num += diff
            if diff <= 0:
                min_num = min(min_num, st_num)
            else:
                max_num = max(max_num, st_num)
        num_gap = max_num - min_num
        range_gap = upper - lower
        # print(num_gap, range_gap)
        return range_gap - num_gap+1 if range_gap >= num_gap else 0


if __name__ == "__main__":
    case = [
        [[1, -3, 4], 1, 6, 2],
        [[3, -4, 5, 1, -2], -4, 5, 4],
        [[4, -7, 2], 3, 6, 0]
    ]
    a = Solution()
    for i in case:
        b = a.numberOfArrays(differences=i[0], lower=i[1], upper=i[2])
        print(b)
        if b != i[3]:
            print('error')
