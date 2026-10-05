class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans=0
        i=0
        for  i in range(len(sequence)-len(word)+1):
            # print(i,sequence[i:i+len(word)])
            j = i
            now_repeat=0
            while sequence[j:j+len(word)] == word:
                now_repeat+=1
                # print(i,now_repeat)
                j+=len(word)
            ans = max(ans,now_repeat)
        return ans


if __name__ == "__main__":
    a = Solution()
    b = a.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba")
    print(b)