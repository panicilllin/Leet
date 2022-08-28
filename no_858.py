import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = p*q/math.gcd(p,q)
        if (lcm/q) %2 ==0:
            return 2
        else:
            if (lcm/p)%2==0:
                return 0
            else:
                return 1

if __name__ == "__main__":
    a = Solution()
    b = a.mirrorReflection(p = 2, q = 1)
    print(b)
# AC
