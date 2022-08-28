import copy
import random
from typing import List


class Solution:
    def recur_sort(self, arr: List):
        if len(arr) <= 1:
            return arr
        middle = int(len(arr) / 2)
        left_child = arr[:middle]
        right_child = arr[middle:]
        left_child = self.recur_sort(left_child)
        right_child = self.recur_sort(right_child)
        arr_new = []
        while True:
            if len(left_child) + len(right_child) == 0:
                break
            elif len(left_child) == 0:
                arr_new.extend(right_child)
                break
            elif len(right_child) == 0:
                arr_new.extend(left_child)
                break
            if left_child[0] <= right_child[0]:
                arr_new.append(left_child.pop(0))
            elif right_child <= left_child:
                arr_new.append(right_child.pop(0))
        return arr_new


if __name__ == "__main__":
    a = Solution()
    b = a.recur_sort(arr=[3, 0, 2, 5, 4, 9, 1, 5, 5, 7, 2, 1])
    print(b)
