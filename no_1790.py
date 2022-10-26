class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        diff=0
        d1 = []
        d2 = []
        for i in range(n):
            c1 = s1[i]
            c2 = s2[i]
            if c1 != c2:
                diff+=1
                d1.append(c1)
                d2.append(c2)
        print(diff,d1,d2)
        if diff == 0 or diff == 2:
            d1.sort()
            d2.sort()
            if d1 == d2:
                return True
        return False