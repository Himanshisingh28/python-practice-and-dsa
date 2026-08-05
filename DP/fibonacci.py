
class Solution(object):
    def fib(self, n):
        memo = {}
        return self.solve(n, memo)
    def solve(self, n, memo):
        if n==0 or n==1:
            return n
        if n in memo: 
            return memo[n]
        memo[n] = self.solve(n-1, memo) + self.solve(n-2,memo)

        return memo[n]
       