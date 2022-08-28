from typing import List


class Solution0:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(0, len(heights)):
            if i != 0 and heights[i] == heights[i-1]:
                continue
            left_end = i
            right_end = i
            for j in range(i, -1, -1):
                if heights[j] < heights[i]:
                    break
                left_end = j
            for k in range(i, len(heights)):
                if heights[k] < heights[i]:
                    break
                right_end = k

            print(f"i {i}, height {heights[i]}, range {left_end},{right_end}, max={heights[i] * (right_end - left_end+1)}")
            res = max(res, heights[i] * (right_end - left_end + 1))
        return res


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        left_i = [0] * n
        right_i = [0] * n
        left_i[0] = -1
        right_i[-1] = n
        for i in range(1, n):
            tmp = i - 1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left_i[tmp]
            left_i[i] = tmp
        for i in range(n - 2, -1, -1):
            tmp = i + 1
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = right_i[tmp]
            right_i[i] = tmp
        print(left_i)
        print(right_i)
        res = 0
        for i in range(n):
            res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        return res


if __name__ == "__main__":
    a = Solution()
    b = a.largestRectangleArea(heights=[2,1,5,6,2,3])
    print(b)
