from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr_col = [row[0] for row in matrix]
        row_num = self.search_by_dichotomy(arr_col, target)
        # if row_num == -1:
        #     return False
        col_num = self.search_by_dichotomy(matrix[row_num], target)
        if col_num == -1:
            return False
        if matrix[row_num][col_num] == target:
            return True
        return False

    def search_by_dichotomy(self, arr, target):
        if len(arr) == 1 and arr[0] <= target:
            return 0
        if not arr[0] <= target <= arr[-1]:
            return -1
        left = 0
        right = len(arr) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if arr[middle] <= target:
                left = middle
            else:
                right = middle

        print(arr, left, right)

        if arr[right] == target:
            return right
        elif arr[left] <= target:
            return left
        else:
            return -1


if __name__ == "__main__":
    a = Solution()
    b = a.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=30)
    print(b)

# AC