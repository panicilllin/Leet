class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        if s1 == s2:
            return True
        else:
            return False

# AC