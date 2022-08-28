class Solution:
    def solveEquation(self, equation: str) -> str:
        left_eq = equation.split('=')[0]
        right_eq = equation.split('=')[1]
        l_x,l_n=self.cal_equation(left_eq)
        r_x,r_n = self.cal_equation(right_eq)
        if l_x - r_x == 0 and r_n-l_n==0:
            return "Infinite solutions"
        elif l_x - r_x == 0:
            return "No solution"
        elif r_n-l_n==0:
            return "x=0"
        # print((r_n-l_n)//(l_x-r_x))
        return f"x={(r_n-l_n)//(l_x-r_x)}"
    def cut_equation(self,equation):
        res_list=[]
        now_num=''
        for val in equation:
            if not now_num:
                now_num+=val
                continue
            if val in ['+','-']:
                res_list.append(now_num)
                now_num = val
            else:
                now_num += val
        res_list.append(now_num)
        # print(res_list)

        return res_list

    def cal_equation(self, equation):
        eq_list=self.cut_equation(equation)
        res_x=0
        res_n=0
        for i in eq_list:
            if i[-1]=='x':
                if len(i)==1:
                    res_x+=1
                elif len(i)==2:

                    if i[0]=='-':
                        res_x-=1
                    elif i[0]=='+':
                        res_x+=1
                    else:
                        res_x+=int(i[0])
                else:
                    if i[0] == '-':
                        res_x -= int(i[1:-1])
                    elif i[0] == '+':
                        res_x += int(i[1:-1])
                    else:
                        res_x += int(i[:-1])
            else:
                if i[0] == '+':
                    res_n += int(i[1:])
                elif i[0] == '-':
                    res_n -= int(i[1:])
                else:
                    res_n += int(i)
        # print(res_x,res_n)
        return res_x,res_n







if __name__ == "__main__":
    a = Solution()
    b = a.solveEquation( equation = "x=x")
    print(b)

    # AC