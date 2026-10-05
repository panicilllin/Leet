class StockSpanner1:
    def __init__(self):
        self.stk = []
        self.cur = 0

    def next(self, price: int) -> int:
        while self.stk and self.stk[-1][1] <= price:
            self.stk.pop()
        prev = -1 if not self.stk else self.stk[-1][0]
        ans = self.cur - prev
        self.stk.append([self.cur,price])
        self.cur += 1
        return ans

class StockSpanner2:
    def __init__(self) -> None:
        self.n=10010
        self.size=110
        self.index=0
        self.nums=[0] *self.n
        self.region=[0]*(self.n//self.size +10)
    
    def get_index(self,x):
        return (x-1) // self.size + 1
    
    def query(self, price):
        ans=0
        loc=self.get_index(self.index)
        left=(loc-1)*self.size+1
        right=self.index
        while loc >= 1 and self.region[loc] <= price:
            ans += right - left +1
            loc -= 1
            
    
    def next(self,price: int) -> int:
        if price%100==0:
            pass
        
        

if __name__ == '__main__':
    a = StockSpanner()
    prices=[100, 80, 60, 70, 60, 75, 85]
    for price in prices:
        b = a.next(price)
        print(b)
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)