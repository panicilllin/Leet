class SolutionFailed:
    def minFlipsMonoIncr(self, s: str) -> int:
        s = list(s)
        for i in range(0,len(s)):
            if s[i] == '0':
                continue
            else:
                s = s[i:]
                break
        print(f"s1 = {s}")
        for i in range(-1,-1-len(s),-1):
            print(f"i2 == {i}")
            if s[i] == '1':
                continue
            else:
                s = s[:i] + [s[i]]
                break
        print(s,s.count('0'))
        return min(s.count('0'),s.count('1'))


class SolutionGreedy:
    def minFlipsMonoIncr(self, s: str) -> int:
        one, zero, ans = 0, 0, 0
        for c in s:
            if c == '1':
                one += 1
            elif c == '0':
                zero += 1
                if one == zero:  # 1和后面出现的0个数相同，此时至少需要翻转其中一半的数字
                    ans += one
                    zero = 0
                    one = 0
                elif zero > 0 and one == 0:  # 前导0，或者前面的0，1翻转后新出现的0可以忽略
                    zero = 0
        if one > zero > 0:
            ans += zero
        return ans

class SolutionDp:
    def minFlipsMonoIncr(self, s: str) -> int:
        one_count = ans = 0
        for c in s:
            if c == '0':
                ans = min(ans+1,one_count)
            else:
                one_count += 1
        return ans
            

if __name__ == '__main__':
 a = SolutionDp()
 b = a.minFlipsMonoIncr("10011111110010111011")
 print(b)