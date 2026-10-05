from typing import List
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.num_dict = {}
        for i in range(0,len(nums)):
            if nums[i] not in self.num_dict:
                self.num_dict[nums[i]] = [i]
            else:
                self.num_dict[nums[i]].append(i)


    def pick(self, target: int) -> int:
        res = self.num_dict.get(target)
        if not res:
            return None
        i = random.randint(0,len(res)-1)
        print(i,res)
        return  res[i]


if __name__ == '__main__':
    a = Solution(nums = [1,2,3,3,3])
    b = a.pick(3)
    print(b)



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)