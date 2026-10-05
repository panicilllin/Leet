from typing import List
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        # print(max(nums))
        cnt=[0] * (max(nums))
        sumn={0:0}
        maxx=0
        # print(cnt)
        res=1
        for i,num  in enumerate(nums):
            if cnt[num-1]>0:
                sumn[cnt[num-1]]-=1
            cnt[num-1]+=1
            if sumn.get(cnt[num-1]):
                sumn[cnt[num - 1]] += 1
            else:
                sumn[cnt[num - 1]] = 1
            maxx = max(maxx,cnt[num - 1])
            if maxx ==1:
                ans=i+1
            elif maxx*sumn[maxx]+1 == i+1:
                ans=i+1
            elif (maxx-1)*(sumn[maxx-1]+1)+1==i+1:
                ans=i+1


        # print(cnt,sumn,maxx)
        return ans
        # print(cnt)



if __name__ == "__main__":
    a = Solution()
    b = a.maxEqualFreq(nums = [2,2,1,1,5,3,3,5])
    print(b)