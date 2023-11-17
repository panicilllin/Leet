from typing import List
import math

class Solution6237:
    def distinctAverages(self, nums: List[int]) -> int:
        res = []
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n//2):
            avg = (nums[i]+nums[-1-i])/2
            if avg not in res:
                res.append(avg)
                ans+=1
        print(res)
        return ans

class Solution6238:
    def lcm(self,x, y):
       #  获取最大的数
        if x > y:
            greater = x
        else:
            greater = y
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm
       
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ans=0
        num_lcm = self.lcm(one,zero)
        times = low//num_lcm
        ans = math.pow((num_lcm//zero + num_lcm//high),times)
        lack = high-times
        
        return ans
                
 
 
if __name__ == "__main__":
    a = Solution6237()
    b = a.distinctAverages([4,1,4,0,3,5])
    print(b)