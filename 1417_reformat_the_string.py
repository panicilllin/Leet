class Solution:
    def reformat(self, s: str) -> str:
        pending_digits=[]
        pending_letters=[]
        for i in s:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                pending_letters.append(i)
            else:
                pending_digits.append(i)
        if abs(len(pending_digits) - len(pending_letters)) >1:
            return ''
        res=''
        if len(pending_digits) > len(pending_letters):
            res = pending_digits.pop()
            for i in range(len(pending_digits)):
                res += pending_letters.pop()
                res+=pending_digits.pop()

        elif len(pending_digits) < len(pending_letters):
            res = pending_letters.pop()
            for i in range(len(pending_digits)):
                res += pending_digits.pop()
                res += pending_letters.pop()
        else:
            res=''
            for i in range(len(pending_digits)):
                res += pending_letters.pop()
                res += pending_digits.pop()
        return res

#AC