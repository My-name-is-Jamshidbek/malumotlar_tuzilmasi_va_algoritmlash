class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ts = 0
        if low % 2 != 0: low -= 1
        if high % 2 != 0: high += 1
        return int((high - low) / 2)
