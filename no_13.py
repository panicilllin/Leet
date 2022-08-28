import copy
class Solution:
    rome_str=['CM','M','CD','D','XC','C','XL','L','IX','X','IV','V','I']
    rome_map={
            'CM':900,
            'M':1000,
            'CD':400,
            'D':500,
            'XC':90,
            'C':100,
            'XL':40,
            'L':50,
            'IX':9,
            'X':10,
            'IV':4,
            'V':5,
            'I':1,
        }
    def romanToInt(self, s: str) -> int:
        if s=='':
            return 0
        res=0
        # print(f"s_new={s}")
        for i in self.rome_str:
            if s[:len(i)]== i:
                res+=self.rome_map[i]
                s=s[len(i):]
                print(i, res,s)
                break
        res += self.romanToInt(s)
        return res

if __name__ == "__main__":
    a = Solution()
    b = a.romanToInt(s = "MCMXCIV")
    print(b)


