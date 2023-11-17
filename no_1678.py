class Solution:
    def interpret(self, command: str) -> str:
        command = list(command)
        n = len(command)
        ans=''
        for i, s in enumerate(command):
            if s == 'G':
                ans += 'G'
            if s == '(' and i < n-1:
                if command[i+1] == ')':
                    ans += 'o'
                if i < n-3 and command[i:i+4] == ['(','a','l',')']:
                    ans += 'al'
        return ans
#AC