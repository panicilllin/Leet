"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        res = []
        child_results = self.generateParenthesis(n-1)
        res.extend(child_results)
        for item in child_results:
            for idx,word in enumerate(item):
                if word == '(':
                    new_item = item[:idx] + '()' + item[idx:]
                    res.append(new_item)


