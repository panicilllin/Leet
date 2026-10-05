class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = list(s)
        max_pair=0
        ans_list=[]
        for i in range(0,len(s)):
            l = i
            r = i
            while l > 0:
                if s[l-1] == s[l]:
                    l-=1
                else:
                    break
            while r < len(s)-1:
                if s[r+1] == s[r]:
                    r+=1
                else:
                    break
            while l > 0 and r < len(s)-1:
                # print(i, l,r)
                if s[l-1] == s[r+1]:
                    l-=1
                    r+=1
                else:
                    break
            # print(i,l,r,s[l:r+1])
            max_pair = max(max_pair,r-l+1)
            if r-l+1 == max_pair:
                ans_list=s[l:r+1]
        ans=''
        for i in ans_list:
            ans+=i
        return ans


if __name__ == "__main__":
    a = Solution()
    b = a.longestPalindrome("abb")
    print(b)
            
                    