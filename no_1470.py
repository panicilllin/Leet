class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)//2
        res=[]
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
# AC