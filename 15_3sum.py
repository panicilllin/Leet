from typing import List


class Solution0:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        re = [nums[i], nums[j], nums[k]]
                        re.sort()
                        if re not in res:
                            res.append(re)
        return res


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 3:
            if len(nums) == 3 and sum(nums) == 0:
                return nums
            else:
                return []
        nums.sort()
        # print(nums)
        res = []
        i = 0

        while nums[i] <= 0:
            l = i + 1
            r = len(nums) - 1

            while l < r:
                re = nums[i] + nums[l] + nums[r]

                if re > 0:
                    r -= 1
                elif re < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # print(res)
                    while l + 1 < r:
                        l += 1
                        if nums[l] != nums[l + 1]:
                            break
                    while l < r:
                        r -= 1
                        if nums[r] != nums[r - 1]:
                            break
                    # print(f"res={res}")
            print(re, [nums[i], nums[l], nums[r]])

            while i + 1 < len(nums):
                i += 1
                if nums[i] != nums[i - 1]:
                    break
        return res


class Solution_others:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 3:
            if len(nums) == 3 and sum(nums) == 0:
                return nums
            else:
                return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                print(f"i={nums[i]},l={nums[l]},r={nums[r]}")
                re = nums[i] + nums[l] + nums[r]
                if re > 0:
                    r -= 1
                elif re < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    print(res)
                    while l < r and nums[l] == nums[l + 1]:
                        l +=i 
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ans = []
        for i in range(n):
            if nums[i] >0:
                break
            j = i+1
            k = n-1
            while(j < k):
                if nums[i]+nums[j]+nums[k] <0:
                    j+=1
                elif nums[i]+nums[j]+nums[k] >0:
                    k-=1
                else:
                    print(i,j,k)
                    if [nums[i],nums[j],nums[k]] not in ans:
                        ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
        return ans
            
            

if __name__ == "__main__":
    a = Solution()
    b = a.threeSum(nums=[-1, 0, 1, 2, -1, -4])
    print(b)
