import copy


class Solution:
    def __init__(self):
        self.cs = None
        self.s = None
        self.exp_dict = {}

    def evaluate(self, expression: str) -> int:
        self.cs = list(expression)
        self.s = copy.deepcopy(expression)
        return self.dfs(0,len(expression)-1,self.exp_dict)

    def dfs(self, l, r, exp_dict):
        if self.cs[l] =='(':
            idx=1
            while (self.cs[idx] != ' '):
                idx +=1
                op = self.s[l+1, idx]
                r-=1
                if op == 'let':
                    pass
                elif op =='add':
                    pass
                elif op == ''





if __name__ == "__main__":
    a = Solution()
    b = a.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))")