from typing import List


class Solution0:
    def maxArea(self, height: List[int]) -> int:
        height_map = {}
        for i, h in enumerate(height):
            if not height_map.get(h):
                height_map[h] = [i]
            else:
                height_map[h].append(i)
        res = 0
        width_stack = []
        for key in sorted(height_map, reverse=True):
            # print(key, height_map[key])
            if not width_stack:
                width_stack = [None, None]
                width_stack[0] = min(height_map[key])
                width_stack[1] = max(height_map[key])
            else:
                width_stack[0] = min(width_stack[0], min(height_map[key]))
                width_stack[1] = max(width_stack[1], max(height_map[key]))
            area = key * (width_stack[1] - width_stack[0])
            # print(area,width_stack)
            res = max(res, area)
        return res


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        res = 0
        while start < end:
            if height[start] >= height[end]:
                res = max(res, (end - start)*height[end])
                end -= 1
            else:
                res = max(res, (end - start)*height[start])
                start += 1
        return res


if __name__ == "__main__":
    a = Solution()
    b = a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(b)
