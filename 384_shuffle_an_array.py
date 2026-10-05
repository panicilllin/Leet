import random
import copy
class Solution:

    def __init__(self, nums):
        self.lst = nums
        self.len = len(self.lst)

    def reset(self):
        return self.lst

    def shuffle(self):
        out = []
        tmp_list = copy.deepcopy(self.lst)

        for i in range(self.len):
            j = random.randint(0, len(tmp_list)-1)
            print(j)
            out.append(tmp_list.pop(j))
        return out
a = Solution([1,2,3,4,5,6])
print(a.shuffle())
print(a.reset())

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()