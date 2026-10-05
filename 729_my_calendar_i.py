from typing import Optional


class Node:
    def __init__(self, val: int, add, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


class MyCalendar_old:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        meet = [start, end-1]
        # gap = {start, end}
        # print(self.calendar)
        if not self.calendar:
            self.calendar.append(meet)
            return True
        for event in self.calendar:
            if event[0] <= meet[0] | event[0] <= meet[1] :
                return False
        self.calendar.append(meet)
        return True

class MyCalendar:
    def book(self, start: int, end: int) -> bool:


if __name__ == "__main__":
    a = MyCalendar()
    b = a.book(10, 20)
    print(b)
    c = a.book(15, 25)
    print(c)
    d = a.book(20, 30)
    print(d)
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
