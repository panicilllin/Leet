from typing import List


class Solution1:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if self.guess_large(event1[1],event2[0]) == False:
            return False
        elif self.guess_large(event2[1],event1[0]) == False:
            return False
        else:
           return True 
    
    def guess_large(self, time1: str, time2:str):
        hour1 = time1.split(":")[0]
        minint1 = time1.split(":")[1]
        hour2 = time2.split(":")[0]
        minint2 = time2.split(":")[1]
        
        if hour1 > hour2:
            return True
        elif hour1 < hour2:
            return False
        else:
            if minint1 > minint2:
                return True
            elif minint1 < minint2:
                return False
            else:
                return None
 
 
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
    
        hcf_num=[]
        for i in range(len(nums)):
            if self.hcf(nums[i],k) == k:
                hcf_num.append(i)
        res=0
        pst=None
        print(hcf_num)
        for i in hcf_num:
            if pst == i-1:
                pst=i
                res+=1
                
            else:
                pst=i
            if nums[i] == k:
                res+=1 
        return res
        
        
    def hcf(self, x, y): 
        if y == 1:
            return y if x==y else x
        for i in range(1,min(x,y) + 1):
            if((x % i == 0) and (y % i == 0)):
                hcf_num = i
        return hcf_num


class Solution3:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pass
        
 
 
 
if __name__ == '__main__':
    a = Solution3()
    b = a.subarrayGCD([3,12,9,6],3)
    print(b)
    