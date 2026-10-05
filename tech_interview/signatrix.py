from typing import *


def demo1(nums:list,target: int) -> bool:
    nums.sort()
    for idxi, itmi in enumerate(nums):
        for idxj, itmj in enumerate(nums[idxi+1:]):
            if itmi+itmj == target:
                return True
    return False


def demo2(nums: list, target:int) -> bool:
    passed_num = [nums[0]]
    # point2=1
    if len(nums) < 2:
        return False
    for i in nums[1:]:
        pass


def demo3(nums: list, target: int) -> bool:
    pass_num = {}
    for i in nums:
        if pass_num.get(target - i, None):
            return True
        pass_num[i] = 1
    return False


# def demo4(nums, target):
#     target_split=[]
#     for i in range()

if __name__ == "__main__":
    a = demo1([1,2,3,9],5)
    print(a)
    b = demo1([1,2,3,9,1,5,4],2)
    print(b)
    c = demo1([1,2,3,9,1,5,4],16)
    print(c)
    d = demo1([1,2,4,4],8)
    print(d)
    e = demo1([],1)
    print(e)