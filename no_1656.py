from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.ptr=1
        self.stream={}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        res=[]
        while self.stream.get(self.ptr):
            res.append(self.stream[self.ptr])
            self.ptr+=1
        return res




# Your OrderedStream object will be instantiated and called as such:
if __name__ == "__main__":

    command=["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
    content=[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
    obj = OrderedStream(content[0][0])
    for i in range(1,len(command)):
        if command[i] == 'insert':
            param = obj.insert(content[i][0],content[i][1])
            print(param)
# AC
S