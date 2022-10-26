class MyLinkedList:

    def __init__(self):
        self.llist = []


    def get(self, index: int) -> int:
        if index >= 0 and  index <= len(self.llist):
            return self.llist[index]
        else:
            return -1


    def addAtHead(self, val: int) -> None:
        self.llist.insert(0,val)


    def addAtTail(self, val: int) -> None:
        self.llist.append(val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index <0 :
            self.addAtHead(val)
        elif 0<= index < len(self.llist):
            self.llist.insert(index,val)
        elif index == len(self.llist):
            self.addAtTail(val)
        else:
            return


    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.llist):
            del self.llist[index]



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)