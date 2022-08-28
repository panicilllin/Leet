class Solution0:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res_s=''
        res_t=''
        for i in s:
            if i == '#':
                res_s=res_s[:-1]
            else:
                res_s+=i
        for j in t:
            if j == '#':
                res_t=res_t[:-1]
            else:
                res_t+=j
        print(res_s,res_t)
        if res_s == res_t:
            return True
        return False

class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # s=s[::-1]
        # t=t[::-1]
        s='0'+s
        t='0'+t
        # print(s,t)
        s_poi=len(s)-1
        t_poi=len(t)-1
        # print(s_poi,t_poi)
        while s_poi>0 and t_poi>0:
            s_back=0
            t_back=0
            # print('====',s[:s_poi+1],t[:t_poi+1])
            while s_poi>0 and s[s_poi] == '#':
                s_poi-=1
                s_back += 1
            while t_poi>0 and t[t_poi] == '#':
                t_poi-=1
                t_back+=1
            s_poi=s_poi - s_back if s_poi > s_back else 0
            t_poi=t_poi - t_back if t_poi > t_back else 0
            # print('----', s_poi,t_poi,s[:s_poi + 1], t[:t_poi + 1])
            # print(s[s_poi],t[t_poi])
            if s[s_poi]=='#' or t[t_poi]=='#':
                continue
            if s[s_poi]!=t[t_poi]:
                return False
            else:
                s_poi-=1
                t_poi-=1

        return True


class Solution:
    def back_space(self,str,poi):
        back = 0
        while poi > 0:
            if str[poi] == '#':
                back += 1
                poi -= 1
            elif back > 0:
                back -= 1
                poi -= 1
            else:
                return poi
        return poi


    def backspaceCompare(self, s: str, t: str) -> bool:
        # s=s[::-1]
        # t=t[::-1]
        s='0'+s
        t='0'+t
        # print(s,t)
        s_poi=len(s)-1
        t_poi=len(t)-1
        while s_poi>0 or t_poi>0:
            s_poi = self.back_space(s, s_poi)
            t_poi = self.back_space(t,t_poi)
            if s_poi >0 and t_poi >0:
                if s[s_poi] != t[t_poi]:
                    return False
            elif s_poi > 0 or t_poi >0 :
                return False
            else:
                s_poi-=1
                t_poi-=1

        return True


if __name__ == "__main__":
    a = Solution()
    b = a.backspaceCompare(s = "a##c", t = "#a#c")
    print(b)
# "y#fo##f"
# "y#f#o##f"
"a##c"
"#a#c"