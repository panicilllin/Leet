from typing import List


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        trends = [0]
        for day in range(1, len(prices)):
            if prices[day] - prices[day - 1] >= 0 and trends[-1] >= 0:
                trends[-1] += prices[day]
            elif prices[day] - prices[day - 1] <= 0 and trends[-1] <= 0:
                trends[-1] += prices[day]
            else:
                trends.append(prices[day] - prices[day - 1])
        print(trends)
        max_profit = 0
        for i in range(len(trends)):
            profit = 0
            for j in range(i + 1, len(trends)):
                profit = trends[j] + profit
                if profit >= max_profit:
                    max_profit = profit
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        trend = [0]
        for day in range(1, len(prices)):
            if prices[day] - prices[day - 1] >= 0 and trend[-1] >= 0:
                trend[-1] += prices[day]
            elif prices[day] - prices[day - 1] < 0 and trend[-1] < 0:
                trend[-1] += prices[day]
            else:
                trend.append(prices[day] - prices[day - 1])
        buy_stack = []
        sell_stack = []
        max_profit = 0
        for i in trend:
            if i >= 0:
                buy_stack.append(i)
            else:
                sell_stack.append(i)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy_day = 0
        sell_day = 1
        max_profit = 0
        while sell_day < len(prices):
            profit = prices[sell_day] - prices[buy_day]
            if profit <= 0:
                buy_day = sell_day
                sell_day += 1
            else:
                max_profit = max(max_profit, profit)
                sell_day += 1
        return max_profit


if __name__ == "__main__":
    a = Solution()
    b = a.maxProfit([1, 2])
    print(b)
