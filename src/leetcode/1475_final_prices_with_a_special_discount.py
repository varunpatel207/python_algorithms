class Solution:
    def finalPrices(self, prices):
        stack = []
        arr = prices[:]
        for i in range(len(prices) - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack:
                arr[i] = arr[i] - stack[-1]
            stack.append(prices[i])
        return arr

s = Solution()
final_prices = s.finalPrices(prices=[8,4,6,2,3])
