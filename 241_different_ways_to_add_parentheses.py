from typing import List


class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:

        res = []
        # print(f"expression={expression}")
        if expression.isdigit():
            return [int(expression)]
        # operator = {i: expression[i] for i in range(0, len(expression)) if not expression[i].isdigit()}

        for op in range(0, len(expression)):
            if expression[op].isdigit():
                continue
            left_val = self.diffWaysToCompute(expression[:op])
            right_val = self.diffWaysToCompute(expression[op + 1:])

            for l_val in left_val:
                for r_val in right_val:
                    res0 = eval(str(l_val) + expression[op] + str(r_val))
                    res.append(res0)
        return res


if __name__ == "__main__":
    a = Solution()
    b = a.diffWaysToCompute("2*3-4*5")
    print(b)
