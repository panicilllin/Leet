from typing import List

class Solution6171:
    def findSubarrays(self, nums: List[int]) -> bool:
        occured=[]
        for i in range(0,len(nums)-1):
            sum_n = nums[i]+nums[i+1]
            if sum_n not in occured:
                occured.append(sum_n)
            else:
                return True
        return False


class Solution6172:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for incre in range(2,n-1):
            strn = self.convert(n,incre)
            replie = self.guess_replie(strn)
            if replie == False:
                return False
        return True
    
    def convert(self,n,incre):
        res=''
        while n != 0:
            res += str(n%incre)
            n = n // incre
        return res
    
    def guess_replie(self, strn):
        for i in range(len(strn)//2):
            if strn[i] != strn[-1-i]:
                return False
        return True
        
        
        

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        row_len = len(mat[0])
        dead_row=[]
        for m, row in enumerate(mat):
            one_count = sum(row)
            if one_count > cols:
                dead_row.append(m)
            if one_count == 0:
                mat[m]=[1 for i in range(row_len)]
                continue
            one_weight = 1/one_count
            for n, num in enumerate(row):
                if num == 1:
                    mat[m][n] = one_weight
        # print(dead_row)
        for row in dead_row[::-1]:
            del mat[row]
        for row in mat:
            print(row)
        print()
        col_count = []
        for i in range(row_len):
            sum_col = 0
            for j in range(len(mat)):
                sum_col += mat[j][i]
            col_count.append([i,sum_col])
        col_count = sorted(col_count, key=lambda x:x[1],reverse=True)
        print(col_count)
        col_count = col_count[:cols]
        res = 0
        for row in mat:
            sum_row = 0
            for colc in col_count:
                col = colc[0]
                sum_row += row[col]
            print(sum_row)
            if sum_row >=1:
                res+=1
        return res
        
            
        
            
if __name__ == "__main__":
    a = Solution()
    b = a.maximumRows([[1,0,1,0,0,0,0,0],[0,0,0,1,1,0,0,1],[0,0,1,1,1,1,1,1],[0,1,0,0,1,1,0,1],[0,1,0,0,1,0,0,0]],5)
    print(b)