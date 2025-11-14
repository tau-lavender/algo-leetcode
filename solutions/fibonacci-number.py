# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        return round(((1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n) / 2 ** n / 5 ** 0.5)
