from tkinter import N


class Solution1:
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


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        start=0
        end=5*k
        while end >= start:
            mid = start+(end-start)//2
            print(f"start={start},mid={mid}, end={end}")
            n=5
            nums = 0
            while n <= mid:
                print(f"n={n}\nnums={nums}\n")
                nums += mid//n
                n = n*5
            if nums == k:
                return 5
            elif nums < k:
                start = mid+1
            else:
                end = mid-1
        return 0

                
if __name__ == '__main__':
    a = Solution()
    b=a.preimageSizeFZF(79)
    print(b)
                
            