class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            res = ''.join(sorted(s))
            return res
        res = s
        for i in range(len(s)):
            new_s = s[i:] + s[:i]
            res = min(res, new_s)
        return res
# AC
