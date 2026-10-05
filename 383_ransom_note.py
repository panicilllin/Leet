class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = {}
        for i in magazine:
            magDict[i] = magDict[i] + 1 if i in magDict else 1

        for i in ransomNote:
            if i not in magDict:
                return False
            elif magDict[i] == 0:
                return False
            else:
                magDict[i] -= 1
        return True

if __name__ == '__main__':
    a = Solution()
    b = a.canConstruct('aa','aab')
    print(b)
# AC