class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) == 0:
            return ''
        elif len(s) == 2:
            return '10'
        count = 0
        last = 0
        substrings = []
        for i in range(len(s)):
            item = s[i]
            if item == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                substring = '1' + self.makeLargestSpecial(s[last + 1:i]) + '0'
                substrings.append(substring)
                # print(s, i, last, substring, substrings)
                last = i + 1
        substrings.sort(reverse=True)
        res = ''
        for substring in substrings:
            res += substring
        # print(s, res)
        return res


if __name__ == "__main__":
    a = Solution()
    b = a.makeLargestSpecial(s="11011000")
    print(b)
