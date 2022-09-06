class Solution:
    def bruteForceMaxProfit(self, prices):
        result = 0
        for bp_index, buy_price in enumerate(prices):
            for sell_price in prices[bp_index + 1:]:
                if sell_price - buy_price <= 0:
                    break
                result = max(result, sell_price - buy_price)

            continue
        return result

    # sliding window
    def maxProfit(self, prices):
        result = 0

        lowest_price_index = 0
        for index, price in enumerate(prices):
            if price < prices[lowest_price_index]:
                lowest_price_index = index
            result = max(result, price - prices[lowest_price_index])

        return result


s = Solution()
profit = s.bruteForceMaxProfit([1,2,4,2,5,7,2,4,9,0,9])
print(profit)