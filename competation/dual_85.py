from typing import List


class Solution1:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        substr = blocks[:k]
        black_count = 0

        for i in substr:
            if i == 'B':
                black_count += 1
        if black_count == k:
            return 0
        max_black = black_count
        # print(substr)
        for i in range(k, len(blocks)):
            # print(i,blocks[i],substr)
            if blocks[i] == substr[0]:
                substr = substr[1:]
                substr += blocks[i]
            else:
                if blocks[i] == 'B':
                    black_count += 1
                    substr = substr[1:]
                    substr += blocks[i]

                    max_black = max(max_black, black_count)
                    if black_count == k:
                        return 0
                else:
                    black_count -= 1
                    substr = substr[1:]
                    substr += blocks[i]
            # print(substr, black_count, max_black)

        return k - max_black


class Solution2:
    def secondsToRemoveOccurrences0(self, s: str) -> int:
        res = 0
        count_0 = 0
        earlest_0 = None
        for i, letter in enumerate(s):
            if letter == '0':
                if earlest_0 == None:
                    earlest_0 = i
                count_0 += 1
        print(count_0, earlest_0)
        return len(s) - count_0 - earlest_0

    def secondsToRemoveOccurrences(self, s: str) -> int:
        res = 0
        s = [int(i) for i in s]
        print(s)
        while True:
            flg = False
            i = 0
            while i < len(s) - 1:
                if s[i:i + 2] == [0, 1]:
                    s[i:i + 2] = [1, 0]
                    i += 2
                    flg = True
                else:
                    i += 1
            if flg is False:
                break
            res += 1
        return res


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyz']
        alphamap = {}
        for i in range(26):
            alphamap[alphabet[i]] = i
        ls = list(s)

        for stru in shifts:
            start = stru[0]
            end = stru[1]
            sub_ls = ls[start:end + 1]
            if stru[2] == 0:
                for i, letter in enumerate(sub_ls):
                    if alphamap[letter] == 0:
                        sub_ls[i] = alphabet[-1]
                    else:
                        sub_ls[i] = alphabet[alphamap[letter] - 1]
            else:
                for i, letter in enumerate(sub_ls):
                    if alphamap[letter] == 25:
                        sub_ls[i] = alphabet[0]
                    else:
                        sub_ls[i] = alphabet[alphamap[letter] + 1]

            ls[start:end + 1] = sub_ls
        res = ''
        # print(ls)
        for letter in ls:
            res += letter
        return res

    def zip_shift(self, s,shifts: List[List[int]]):
        move=[0 for i in range(len(s))]
        print(move)
        for i in shifts:
            if i[2]==0:
                move[i[0]:i[1]+1]= [i+1 for i in move[i[0]:i[1]+1] ]
            else:
                move[i[0]:i[1]+1]= [i-1 for i in move[i[0]:i[1]+1] ]

        lphabet = [i for i in 'abcdefghijklmnopqrstuvwxyz']
        alphamap = {}
        for i in range(26):
            alphamap[alphabet[i]] = i
        for i in move:
            




if __name__ == "__main__":
    a = Solution()
    b = a.zip_shift(s="dztz", shifts=[[0, 0, 0], [1, 1, 1]])
    print(b)
