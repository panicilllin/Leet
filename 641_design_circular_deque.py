class MyCircularDeque:

    def __init__(self, k: int):
        self.list_len=k
        self.list = []


    def insertFront(self, value: int) -> bool:
        if self.isFull() is True:
            return False
        else:
            self.list.insert(0,value)
            return True


    def insertLast(self, value: int) -> bool:
        if self.isFull() is True:
            return False
        else:
            self.list.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty() is True:
            return False
        self.list.pop(0)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty() is True:
            return False
        self.list.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty() is True:
            return -1
        return self.list[0]

    def getRear(self) -> int:
        if self.isEmpty() is True:
            return -1
        return self.list[-1]

    def isEmpty(self) -> bool:
        if len(self.list)==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        # print(self.list_len,self.list)
        if len(self.list)>=self.list_len:
            return True
        else:
            return False


if __name__ == "__main__":
# Your MyCircularDeque object will be instantiated and called as such:
    obj = MyCircularDeque(3)
    param_1 = obj.insertLast(1)
    param_2 = obj.insertLast(2)
    param_3 = obj.insertFront(3)
    param_4 = obj.insertFront(4)
    param_5 = obj.getRear()
    param_6 = obj.isFull()
    param_7 = obj.deleteLast()
    param_8 = obj.insertFront(4)
    param_9 = obj.getFront()
    print(param_1,param_2,param_3,param_4,param_5,param_6,param_7,param_8,param_9)