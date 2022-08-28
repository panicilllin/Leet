class LineNode:
    def __init__(self, start, end):
        self.index = None
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.mark = 0

    def left_child(self,index:int):
        return 2*index+1

    def add_mark(self, value):
        self.mark += value

    def clear_mark(self):
        self.mark = 0

class Solution:


    def build_tree(lines,tree=None):
        tree = [None] * (4 * len(lines)) if not tree else tree
        lines.sort()






if __name__ == "__main__":
    a = LineNode()
    b = tree(10, 20)
    print(b)
    c = a.book(15, 25)
    print(c)
    d = a.book(20, 30)
    print(d)