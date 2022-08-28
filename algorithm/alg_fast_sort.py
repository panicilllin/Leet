import copy
import random
from typing import List


class Solution:

    def fast_sort(self, arr: List, num: int = None, min_array: int = None, max_array: int = None) -> List:
        num = random.choice(arr) if not num else num
        min_idx = 0 if min_array is None else copy.deepcopy(min_array)
        max_idx = len(arr) - 1 if max_array is None else copy.deepcopy(max_array)

        # print(
        #     f"======\n"
        #     f"arr={arr}\n"
        #     f"arr_short={arr[min_array:max_array+1]}\n"
        #     f"num={num},min={min_idx},max={max_idx}\n"
        # )

        if min_idx >= len(arr) - 1 or max_idx == 1 or max_idx <= min_idx:
            return arr

        i = min_idx
        while True:

            if i > max_idx:
                break
            if arr[i] < num:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                min_idx += 1
                i += 1
            elif arr[i] == num:
                i += 1
            else:
                arr[i], arr[max_idx] = arr[max_idx], arr[i]
                max_idx -= 1
        # print(f"---left----\narr={arr}\n"
        #       f"min1={min_array},min={min_idx}\n"
        #       f"arr_l={arr[min_array:min_idx]}")
        if arr[min_array:min_idx]:
            arr = self.fast_sort(arr, num=random.choice(arr[min_array:min_idx]),
                             min_array=min_array, max_array=min_idx-1)
        # print(f"---right----\narr={arr}\n"
        #       f"max={max_idx},max1={max_array}\n"
        #       f"arr_r={arr[max_idx + 1:max_array + 1]}")
        if arr[max_idx + 1:max_array+1]:
            arr = self.fast_sort(arr, num=random.choice(arr[max_idx + 1:max_array+1]),
                             min_array=max_idx + 1, max_array=max_array)
        return arr


if __name__ == "__main__":
    a = Solution()
    b = a.fast_sort(arr=[3, 0, 2, 5, 4, 9, 1, 5, 5, 7, 2, 1, 7, 6, 8, 4,5], num=5, min_array=0, max_array=16)
    print(b)
