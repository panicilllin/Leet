class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 26 up one
        res = ''
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # columnNumber -= 1
        while columnNumber > 26:
            print(columnNumber//26, columnNumber%26)
            res = alphabet[columnNumber%26 -1] + res
            columnNumber = (columnNumber-1)//26
            print(res, columnNumber)
        print(columnNumber)
        res = alphabet[columnNumber-1] + res
        return res

if __name__ == "__main__":
    a = Solution()
    b = a.convertToTitle(27)
    print(f"final = {b}")