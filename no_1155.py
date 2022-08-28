class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n > target or n*k < target:
            return 0
        if n == target or n*k == target:
            return 1

    def roll(self,n,k,target,):

if __name__ == "__main__":
    a = Solution()
    b = a.numRollsToTarget(30,30,500)