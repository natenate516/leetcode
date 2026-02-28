class Solution(object):
    def buyChoco(self, prices, money):
        smallest = float('inf')
        secondSmallest = float('inf')
        for price in prices:
            if price < smallest:
                secondSmallest = smallest
                smallest = price
            elif price < secondSmallest:
                secondSmallest = price

        total = smallest + secondSmallest
        if total > money:
            return money
        else:
            return money - total