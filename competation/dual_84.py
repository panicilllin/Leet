import math
from collections import Counter
from typing import List


class Solution1:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = {}
        for object in items1:
            value = object[0]
            weight = object[1]
            if not res.get(value):
                res[value] = weight
            else:
                res[value] += weight
        for object in items2:
            value = object[0]
            weight = object[1]
            if not res.get(value):
                res[value] = weight
            else:
                res[value] += weight
        ret = []
        for value in res.keys():
            ret.append([value, res[value]])
        ret.sort(key=lambda obj: obj[0])
        return ret


class Solution2:
    def countBadPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(1,len(nums)):
            for j in range(i+1, len(nums)):
                # print(i, j)
                if j - i != nums[j] - nums[i]:
                    res += 1
        return res

class Solution2_2:
    def countBadPairs(self, nums: List[int]) -> int:
        res = 0
        print(len(nums))
        moves=[item-i for i,item in enumerate(nums)]
        max_move = max(set(moves), key=moves.count)
        max_count = moves.count(max_move)

        print(max_move,max_count,[i-max_move for i in moves])
        last_num = len(nums)-1
        n_num = len(nums)-max_count
        first_num = last_num-n_num+1

        res=0
        print(first_num,last_num,n_num)
        for i in range(first_num+1, last_num+1):
            res+=i

        return res

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        rest_map={}
        day=0
        for task in tasks:

            if not rest_map.get(task):
                day+=1
                print(f"day={day},task={task}")
                rest_map[task] = day
            else:
                gap_time=day-rest_map[task]
                rest_time = space-gap_time
                # print(f"rest_time={rest_time}")
                if rest_time<=0:
                    day += 1
                else:
                    day+=rest_time+1
                print(f"day={day},task={task}")
                rest_map[task] = day
        return day

if __name__ == "__main__":
    a = Solution()
    b = a.taskSchedulerII(tasks = [5,8,8,5], space = 2)
    print(b)