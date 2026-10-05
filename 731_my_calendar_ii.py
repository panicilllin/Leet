class MyCalendarTwo:

    def __init__(self):


    def book(self, start: int, end: int) -> bool:



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


if __name__ == "__main__":
    a = MyCalendarTwo()
    b = a.book(10, 20)
    c = a.book(50, 60)
    d = a.book(10, 40)
    e = a.book(5, 15)
    f = a.book(5, 10)
    g = a.book(25, 55)


    print(b)