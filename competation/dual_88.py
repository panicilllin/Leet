from typing import List


class Solution1:
    def equalFrequency(self, word: str) -> bool:
        alpha_dict = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i in word:
            alpha_dict[i] += 1
        # print(alpha_dict)
        values={}
        for value in alpha_dict.values():
            if value == 0:
                continue
            if values.get(value) == None:
                values[value] = 1
            else:
                values[value] += 1
        print(values)
        if len(values) == 0:
            return False
        elif len(values) == 1:
            keys = [i for i in values.keys()]
            if keys[0] == 1:
                return True
        elif len(values) == 2:
            keys = [i for i in values.keys()]
            keys.sort()
            print(keys)
            if keys[1] == keys[0] + 1:
                if 1 in [values[keys[0]], values[keys[1]]]:
                    return True
        return False

class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.list=[None for i in range(n+1)]
        self.list[0]=1
        self.idx = 0

    def cal_longest(self):
        res = self.idx
        for i in range(self.idx, self.n+1):
            if self.list[i] == None:
                break
            res=i
        return res

    def upload(self, video: int) -> None:
        if video > self.n:
            return False
        self.list[video] = 1



    def longest(self) -> int:
        idx = self.cal_longest()
        self.idx = idx
        if idx <=0:
            return 0
        else:
            return self.idx



class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        arr=[]
        for i in nums1:
            for j in nums2:
                arr.append(i^j)

        print(arr)
        res = arr[0]
        for i in arr[1:]:
            res = res^i
        return res



if __name__ == '__main__':
    a = Solution()
    b = a.xorAllNums([1,2],[3,4])
    print(b)