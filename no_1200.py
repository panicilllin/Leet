from typing import List
from collections import defaultdict


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        len_dict = defaultdict(list)
        min_len = arr[-1] - arr[0]
        # print(min_len)
        for i in range(0, len(arr) - 1):
            m_len = arr[i + 1] - arr[i]
            # print(f"mlen={m_len}")
            if m_len <= min_len:
                len_dict[m_len].append([arr[i], arr[i + 1]])
                min_len = m_len
        # print(len_dict)
        # print(min_len)
        return len_dict[min_len]


if __name__ == "__main__":
    a = Solution()
    b = a.minimumAbsDifference([1, 3, 6, 10, 15])
    print(b)
