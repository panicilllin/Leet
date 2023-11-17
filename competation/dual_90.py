from mimetypes import common_types
from re import A
from typing import List


class Solution1:
    def oddString(self, words: List[str]) -> str:
        n = len(words[0])
        alpha=[]
        alpha_dict = {}
        ans=None
        for word in words:
            idx=[None]*(n-1)
            for i in range(n-1):
                idx[i] = ord(word[i+1])-ord(word[i])
            # print(idx,len(alpha))
            
             
            if len(alpha) == 0 and idx not in alpha:
                alpha.append(idx)
                alpha_dict[str(idx)] = word 
            elif len(alpha) == 1 and idx not in alpha:
                ans=word
                alpha.append(idx)
                alpha_dict[str(idx)] = word  
            elif len(alpha) > 1:
                print(idx,alpha,alpha_dict)
                for i in alpha:
                    if i != idx:

                        ans = alpha_dict.get(str(i))
                        return ans
            # print(alpha,alpha_dict)
        return ans
 
 
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        n = len(queries[0])
        for i in queries:
            for j in dictionary:
                if self.diff_words(n,i,j) is True:
                    ans.append(i)
                    break
        return ans
        
    def diff_words(self, n, w1, w2):
        ans = 0
        for i in range(n):
            if w1[i]!=w2[i]:
                ans+=1
            if ans > 2:
                return False
        if ans <=2:
            return True
    

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
       
  
if __name__ == "__main__":
    a = Solution()
    b = a.destroyTargets(nums = [3,7,8,1,1,5], space = 2)
    print(b)