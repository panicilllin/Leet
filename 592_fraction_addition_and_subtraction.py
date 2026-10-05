import copy
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression if expression[0] == '-' else '+' + expression
        fractions = []
        expression_new = copy.deepcopy(expression)
        i = 0
        j = 0
        for i in range(0, len(expression)):
            if expression[i] in ['+', '-']:
                fractions.append(expression[j:i])
                j = i
        fractions.append(expression[j:])
        if fractions[0] == '':
            fractions = fractions[1:]
        # print(fractions)
        denominators = [int(i.split('/')[-1]) for i in fractions]
        lcm = self.Least_common_multiple(denominators)
        numerators = [int(i.split('/')[0][1:]) for i in fractions]
        operators = [i.split('/')[0][0] for i in fractions]
        numer = 0
        for i in range(0, len(fractions)):
            plus = int(lcm / denominators[i])
            operator = operators[i]
            numerator = numerators[i]
            # print(f"plus={plus},op={operator},num={numerator},numer={numer}")
            if operator == '+':
                numer += numerator*plus
            elif operator == '-':
                numer -= numerator*plus
        if numer == 0:
            return '0/1'
        minimum = self.Maximum_common_divisor([abs(numer), lcm])
        res = '' if numer > 0 else '-'
        numer = int(abs(numer)/minimum)
        denom = int(lcm/minimum)
        res = res + str(numer) + '/' + str(denom)
        return res

    def Least_common_multiple(self,num):  # 求任意多个数的最小公倍数
        minimum = 1
        for i in num:
            minimum = int(i) * int(minimum) / math.gcd(int(i), int(minimum))
        return int(minimum)

    def Maximum_common_divisor(self,num):  # 求任意多个数的最大公约数
        minimum = max(num)
        for i in num:
            minimum = math.gcd(int(i), int(minimum))
        return int(minimum)


if __name__ == "__main__":
    a = Solution()
    b = a.fractionAddition(expression="1/3-1/2")
    print(b)


# AC