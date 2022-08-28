from typing import  List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda k_first: k_first[0])
        # print(intervals)
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1] >= intervals[i][1]:
                continue
            elif res[-1][1] >= intervals[i][0]:
                res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        return res


if __name__ == '__main__':
    a = Solution()
    b = a.merge(intervals = [[1,3],[2,6],[8,10],[15,18]])
    print(b)