class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        max_length = 0
        for i, _ in enumerate(s):
            tmp_list = []
            max_length = 0
            # print(i,tmp_list,max_length)
            for j, cha in enumerate(s[i:]):
                if cha in tmp_list:
                    ans = max(ans, max_length)
                    print(i,j,tmp_list)
                    break
                else:
                    tmp_list.append(cha)
                    max_length+=1
                ans = max(ans, max_length)
                print(i,j,tmp_list)
                
        ans = max(ans,max_length)
        return ans

if __name__ == "__main__":
    a = Solution()
    b = a.lengthOfLongestSubstring("")
    print(b)
        
 # AC