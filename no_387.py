class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabet={i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for l in s:
            alphabet[l]+=1
        for i,l in enumerate(list(s)):
            if alphabet[l]==1:
                return i
        return -1

if __name__ == "__main__":
    a = Solution()
    b = a.firstUniqChar(s = "leetcode")
    print(b)

#AC
