from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        deep=0
        for act in logs:
            if act == './':
                continue
            elif act == '../':
                if deep > 0:
                    deep -= 1
            else:
                deep += 1
        return deep
