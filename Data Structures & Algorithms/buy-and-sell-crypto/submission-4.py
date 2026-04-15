class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diffs = []
        for i in range(len(prices) - 1):
            rest = prices[i + 1:]
            diffs.append(max(rest) - prices[i])
        if len(diffs) == 0 or max(diffs) < 0:
            return 0
        return max(diffs)   