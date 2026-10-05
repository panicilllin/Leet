"""
Meeting Rooms II
Medium

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000

Hint 1
Try to visualize the meetings as line segments on a number line representing start and end times. The number of rooms required is the maximum number of overlapping meetings at any point on the number line. Can you think of a way to determine this efficiently?


Hint 2
We create two arrays, start and end, containing the start and end times of all meetings, respectively. After sorting both arrays, we use a two-pointer based approach. How do you implement this?


Hint 3
We use two pointers, s and e, for the start and end arrays, respectively. We also maintain a variable count to track the current number of active meetings. At each iteration, we increment s while the start time is less than the current end time and increase count, as these meetings must begin before the earliest ongoing meeting ends.


Hint 4
Then, we increment e and decrement count as a meeting has ended. At each step, we update the result with the maximum value of active meetings stored in count.
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        starts.sort()
        ends.sort()
        s = 0
        e = 0
        count = 0
        res = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res

class Solution_heap:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

if __name__ == '__main__':
    a = Solution()
    b = a.minMeetingRooms(intervals = [(0,40),(5,10),(15,20)])
    print(b)