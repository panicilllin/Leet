from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # find zero
        pos_list=[]
        neg_list=[]
        res = []
        for i in range(0, len(nums)):
            if nums[i] < 0:
                neg_list.insert(0, nums[i])
            else:
                pos_list = nums[i:]
                break
        i = j = 0
        while i < len(pos_list) and j < len(neg_list):
            if pos_list[i] < abs(neg_list[j]):
                res.append(pos_list[i]*pos_list[i])
                i += 1
            else:
                res.append(neg_list[j]*neg_list[j])
                j += 1
        if i < len(pos_list):
            for num in pos_list[i:]:
                res.append(num*num)
        if j < len(neg_list):
            for num in neg_list[j:]:
                res.append(num*num)
        # print(pos_list)
        # print(neg_list)
        return res
        
if __name__ == '__main__':
    a = Solution()
    b = a.sortedSquares(nums = [-4,-1,0,3,10])
    print(b)