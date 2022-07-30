class Solution:
    def reverse(self, x: int) -> int:
        ret = int(str(x).replace("-", "")[::-1]) * (-1 if x < 0 else 1) 
        return ret if abs(ret) < 2 ** 31 else 0


sol = Solution()
print(sol.reverse(-567))