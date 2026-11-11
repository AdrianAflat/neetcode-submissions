class StockSpanner:

    def __init__(self):
        self.count = 0
        self.stack = [] # [price, count]

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        self.count += 1
        
        if self.stack:
            span = self.count - self.stack[-1][1]
        else:
            span = self.count

        self.stack.append([price, self.count])
        return span
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# 100, 80, 60, 70, 60, 75, 85
#  1    1  1.  2.  1.   4.  6

# [(100, 1), (85, 7)]