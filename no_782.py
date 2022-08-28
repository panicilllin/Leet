class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        row_arr,col_arr = self.guess_chessable(board)
        if not row_arr:
            return -1
        print(row_arr,col_arr)
        ans=0
        ans+=self.chessable(row_arr)
        ans+=self.chessable(col_arr)
        return ans

    def chessable(self,array):
        arr1  =  array.pop(0) if len(array[0]) >= len(array[1]) else array.pop(1)
        arr2 = array[0]
        if len(arr1) == len(arr2):
            even=0
            for i in arr1:
                if i%2 == 0:
                    even+=1
            return min(even,len(arr1)-even)

        elif len(arr1) > len(arr2):
            even = 0
            for i in arr1:
                if i % 2 == 0:
                    even += 1
            return len(arr1) - even
        else:
            print("ERRRRRR")



    def guess_chessable(self,board):
        row_map={}
        def list_to_str(list):
            res=''
            for i in list:
                res+=str(i)
            return res

        def count_even(list):
            even=0
            for i in list:
                if i%2==0:
                    even+=1
            if abs(len(list) -even*2)>1:
                return False
            return True

        for i,row in enumerate(board):
            row_str = list_to_str(row)
            if row_map.get(row_str):
                row_map[row_str].append(i)
            else:
                if not count_even(row):
                    return False, False
                row_map[row_str] = [i]
        if len(row_map) != 2:
            return False,False

        col_map={}
        for j in range(len(board)):
            col = [row[j] for row in board]
            col_str = list_to_str(col)
            if col_map.get(col_str):
                col_map[col_str].append(j)
            else:
                if not count_even(col):
                    return False, False
                col_map[col_str] = [j]
        if len(col_map) != 2:
            return False,False
        row_list = [row_map[k] for k in row_map.keys()]
        col_list = [col_map[k] for k in col_map.keys()]
        return row_list,col_list

#AC