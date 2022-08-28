class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        
        while n > 1:
            if n %3 != 0:
                return False
            n = int(n/3)
        if n == 1:
            return True
        else:
            return False
#AC