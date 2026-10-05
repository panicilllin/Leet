import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(a) > len(b):
            return -1
        count = math.ceil(len(b)/len(a))
        min_a = a*count
        if b in min_a:
            return count
        for i in range(1,3):
            min_a = min_a + a
            count += 1
            if b in min_a+a:
                return count

        return -1

if __name__ == "__main__":
    a=Solution()
    b = a.repeatedStringMatch(a="abcd", b = "cdabcdab")
    print(b)
