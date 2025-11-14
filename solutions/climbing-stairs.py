# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (1, 2):
            return n
        else:
            a = 1
            b = 2
            c = 2
            while c < n:
                a, b = b, a + b
                c += 1
            return b
