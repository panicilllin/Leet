from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i,price in enumerate(prices):
            for discount in prices[i+1:]:
                if discount <= price:
                    prices[i]=price-discount
                    break
        return prices
# AC