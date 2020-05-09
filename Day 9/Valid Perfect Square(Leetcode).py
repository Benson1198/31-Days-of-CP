class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        square_root = num ** 0.5
        mod1 = square_root % 1
        is_perf_squ = (mod1 == 0)
        return is_perf_squ