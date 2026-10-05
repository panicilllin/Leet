from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        if arr_len == 0:
            return []
        if arr_len ==1:
            return [1]
        arr_new = [[arr[i],i,None] for i in range(0,arr_len)]
        arr_new.sort(key=lambda first_k: first_k[0])
        arr_new[0][2] = 0
        for i in range(1, arr_len):
            if arr_new[i][0] == arr_new[i-1][0]:
                arr_new[i][2] = arr_new[i-1][2]
            else:
                arr_new[i][2] = arr_new[i - 1][2] + 1
        print(arr_new)
        res = [0]*arr_len
        for i in range(0, arr_len):
            position = arr_new[i][1]
            res[position] = arr_new[i][2] +1
        return res



if __name__ == '__main__':
    a = Solution()
    b = a.arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12])
    print(b)