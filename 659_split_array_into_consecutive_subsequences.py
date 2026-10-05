class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        last_sub=[]
        for i, num in enumerate(nums):
            if not last_sub:
                last_sub.append(num)
            elif last_sub[-1] == num-1:
                last_sub.append(num)
            else:
                if len(last_sub)<3:
                    return False
                else:
                    last_sub = [num]
        if last_sub and len(last_sub)<3:
            return False
        return True
