class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(n+1):
            if self.cal_rotate(i) == True:
                res+=1
        return res
    
    
    def cal_rotate(self, num: int) -> bool:
        num_arr = [int(i) for i in list(str(num))]
        flg = False
        for i in num_arr:
            if i in [0,1,8]:
                continue
            elif i in [2,5,6,9]:
                flg = True
            else:
                return False
        if flg:
            return True
        else:
            return False

if __name__ == '__main__':
    a = Solution()
    b = a.rotatedDigits(10)
    print(b)

# AC