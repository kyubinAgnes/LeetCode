class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def f(n, k):
            if n == 1:
                return 0
            return f(n - 1, k // 2) if k % 2 == 0 else 1 - f(n - 1, k // 2)
        k -= 1
        return f(n, k)