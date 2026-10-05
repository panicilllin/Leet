class PeekingIterator:

    def __init__(self, iterator):
        self.array = []
        self.pointer = -1
        self.len = len(self.array)

    def has_next(self):
        if self.pointer >= self.len:
            return False
        return True

    def next(self):
        self.pointer += 1
        if self.pointer >= self.len:
            return False
        return self.array[self.pointer]


    def peek(self):
        if self.has_next():
            return self.array[self.pointer+1]


def run(conduct_list, contain_list):
    return_list = []
    iter_obj = False
    for i in range(0, max(len(conduct_list), len(contain_list))):
        cond = conduct_list[i]
        cont = contain_list[i]
        # print(cond,cont)
        if cond == 'PeekingIterator':
            iter_obj = Iterator(cont[0])
            return_list.append('null')
        if cond == 'hasNext' and iter:
            res = iter_obj.has_next()
            return_list.append(res)
        if cond == 'next' and iter:
            res = iter_obj.next()
            return_list.append(res)
        if cond == 'peek' and iter:
            res = iter_obj.peek()
            return_list.append(res)
    return return_list

if __name__ == '__main__':
    res = run(["PeekingIterator", "next", "peek", "next", "next", "hasNext"], [[[1, 2, 3]], [], [], [], [], []])
    print(res)