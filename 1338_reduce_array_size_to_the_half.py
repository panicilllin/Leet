from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        num_occur={}
        for i in arr:
            if not num_occur.get(i):
                num_occur[i] = 1
            else:
                num_occur[i] += 1

        val=list(num_occur.values())
        val.sort(reverse=True)

        sum=0
        n = len(arr)
        for i,v in enumerate(val):
            sum+=v
            if sum*2>=n:
                return i+1
        return n

if __name__ == "__main__":
    a = Solution()
    b = a.minSetSize(arr = [1,9])
    print(b)