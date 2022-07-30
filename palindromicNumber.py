class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        cur = x
        while cur > 0:
            digits.append(cur % 10)
            cur = cur // 10
        i = 0
        j = len(digits) - 1
        while i <= j:
            if digits[i] != digits[j]:
                return False
            i += 1
            j -= 1
        return True


print(Solution().isPalindrome(5005))