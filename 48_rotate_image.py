from typing import List
import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ceilm = math.ceil(n/2)
        floorm = math.floor(n/2)
        for i in range(ceilm):
            for j in range(floorm):
                a = [i,j]
                b = [j,n-1-i]
                c = [n-1-i,n-1-j]
                d = [n-1-j,i]
                # print(a,b,c,d)
                num_a = matrix[a[0]][a[1]]
                num_b = matrix[b[0]][b[1]]
                num_c = matrix[c[0]][c[1]]
                num_d = matrix[d[0]][d[1]]
                print(a,num_a,b,num_b,c,num_c,d,num_d)
                matrix[b[0]][b[1]] = num_a
                matrix[c[0]][c[1]] = num_b
                matrix[d[0]][d[1]] = num_c
                matrix[a[0]][a[1]] = num_d
        return matrix

if __name__ == '__main__':
    a = Solution()
    b=a.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
    print(b)
#AC