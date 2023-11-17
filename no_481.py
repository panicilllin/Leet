class Solution:
    def magicalString(self, n: int):
        if n < 4:
            return 1
        magic_list = [None]*n
        magic_list[:3]= [1,2,2]
        idx = 1
        idx_len = 3
        ans = 1
        while idx_len < n:
            idx+=1
            last_num = magic_list[idx_len-1]
            next_block = magic_list[idx]
            if next_block == 1:
                if last_num == 1:
                    magic_list[idx_len] = 2
                else:
                    magic_list[idx_len] = 1
                    ans += 1
                idx_len+=1
            else:
                if last_num == 1:
                    magic_list[idx_len:idx_len+2] = [2,2]
                else:
                    magic_list[idx_len:idx_len+2] = [1,1]
                    if n-idx_len <2 :
                        ans+=1
                    else:
                        ans+=2
                idx_len+=2
                    
        print(magic_list)
        return ans

if __name__ == "__main__":
    a = Solution()
    b = a.magicalString(n=15)
    print(b)
    
            