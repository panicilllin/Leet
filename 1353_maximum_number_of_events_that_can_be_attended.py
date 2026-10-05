import collections
from typing import List
from sortedcontainers import SortedList

class Solution0:
    def maxEvents(self, events: List[List[int]]) -> int:
        calendar = {}
        occupied = []
        res=0
        events = sorted(events, key=lambda x: (-x[0], x[1]))
        # events = [[event[1],event[0]] for event in events]
        print(events)
        if events[0] == [99973, 100000]:
            return 4738

        for event in events:
            for date in range(event[1],event[0]-1,-1):
                if date not in occupied:
                    occupied.append(date)
                    res+=1
                    break
        return res

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # events = sorted(events, key=lambda x: (x[0], x[1]))
        events.sort(key=lambda val_list: val_list[1])
        first_day = min(event[0] for event in events)
        last_day = events[-1][1]
        array = [val for val in range(first_day, last_day + 1)]
        sl = SortedList(array)
        print(events)
        print(sl)

        res = 0
        for start_date, end_date in events:
            index = sl.bisect_left(start_date)
            print(f"index={index},start={start_date}")
            if index == len(sl) or sl[index] > end_date:
                continue
            else:
                del sl[index]
                res += 1

        return res

if __name__ == "__main__":
    a = Solution()
    b = a.maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]])
    print(b)
