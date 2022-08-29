class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        if k <5:
            return 0
        jump_l=[]
        i=0
        while True:
            i+=1
            for j in range(i):
                jump_num=j+5**i
                print(jump_num)
                if jump_num == k:
                    return 0
                if jump_num > k:
                    return 5
                jump_l.append(jump_num)


if __name__ == '__main__':
    a = Solution()
    b=a.preimageSizeFZF(79)
    print(b)
                
            