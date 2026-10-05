class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row=[0]
        for i in range(0,n-1):
            print(row)
            j=0
            while 
            for j in range(len(row)):
                if j == 0:
                    row.insert(j+1,1)
                else:
                    row.insert(j+1,0)
        print(row)
        return row[k-1]

if __name__ == '__main__':
    a = Solution()
    b = a.kthGrammar(3,3)
    print(b)