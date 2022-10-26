from pyexpat import native_encoding
from typing import List


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nagetive_list=[]
        zero_list=[]
        positive_list=[]

        for i in nums:
            if i < 0:
                nagetive_list.append(i)
            elif i == 0:
                zero_list.append(i)
            else:
                positive_list.append(i)
        
        
        