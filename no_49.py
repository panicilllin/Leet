from signal import alarm
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # alphabet = [0]*26
        alphadict={}
        for i, str in enumerate(strs):
            alphalist = [0]*26
            for k in str:
                alphalist[ord(k)-ord('a')] +=1
            # print(alphalist)
            alpha_key = "% s" % alphalist
            if not alphadict.get(alpha_key):
                alphadict[alpha_key] = []
            alphadict[alpha_key].append(str)
        ans = []
        for value in alphadict.values():
            ans.append(value)
        return ans

if __name__ == '__main__':
    a = Solution()
    b = a.groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"])
    print(b)
# AC        