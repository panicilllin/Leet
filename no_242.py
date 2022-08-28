class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_dict = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i in s:
            letter_dict[i] += 1
        for i in t:
            letter_dict[i] -= 1
        for i in letter_dict.values():
            if i != 0:
                return False
        return True
# AC
