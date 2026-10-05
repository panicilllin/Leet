from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[-1], x[0]))
        print(intervals)
        res_l = intervals[0][0] - 1
        res_r = intervals[0][-1]
        print(res_l, res_r)
        res = 2
        for i in range(1, len(intervals)):

            interval = intervals[i]
            interval_l = interval[0]
            interval_r = interval[-1]
            print(f"res_l={res_l}, res_r={res_r}")
            print(f"int_l={interval_l},int_r={interval_r}")
            if interval_l > res_r:
                res += 2
                res_r = interval_r
            elif interval_l == res_r or interval_l > res_l:
                res += 1
                res_l = res_r
                res_r = interval_r
        return res


if __name__ == "__main__":
    a = Solution()
    b = a.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]])
    print(b)
