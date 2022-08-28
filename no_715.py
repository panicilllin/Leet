class RangeModule:

    def __init__(self):

        self.range = []

    def addRange(self, left: int, right: int) -> None:
        if not self.range:
            self.range.append([left, right])
        else:
            if right < self.range[0][0]:
                self.range.insert(0,[left,right])
            elif right == self.range[0][0]:
                self.range[0][0] = left
            elif left > self.range[-1][1]:
                self.range.append([left,right])
            elif left == self.range[-1][1]:
                self.range[-1][1] = right
            else:
                for i in (0, len(self.range)):
                    if i == 0:
                        if right < self.range[i][0]:
                            self.range.insert(0, [left, right])
                        elif right == self.range[i][0]:
                            self.range[0][0] = left
                        elif
                    if self.range[i-1][0] < left and right < self.range[i-1][1]:
                        return
                    if self.range[i-1][1] < left and  right < self.range[i][0]:
                        self.range.insert(i,[left,right])
                    elif self.range[i-1][1] >= left and right < self.range[i][0]:
                        self.range[i-1][1] = right
                    elif self.range


    def queryRange(self, left: int, right: int) -> bool:


    def removeRange(self, left: int, right: int) -> None:



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)