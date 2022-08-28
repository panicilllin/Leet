class Solution:
    def reverseBits(self, n: bin) -> int:
        # bin_n = bin(n)
        str_bin = str(n)
        # print(str_bin)
        rev_str = str_bin[::-1]
        # print(rev_str)
        sum = 0
        for i in range(len(rev_str)):
            sum += int(rev_str[i])*2**(len(rev_str)-i-1)

        return rev_str

class Solution2:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1)|(n&1)
            n >>=1
        return res

if __name__ == "__main__":
    a = Solution()
    b = a.reverseBits(n = 11111111111111111111111111111101)
    print(b)
