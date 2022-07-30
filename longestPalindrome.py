class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        start = 0
        full_len = len(s)
        dp = [[True if i == j else False for i in range(full_len)] for j in range(full_len)]
        
        for i in range(full_len - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
            else:
                dp[i][i+1] = False
        
        sub_len=3
        while sub_len <= full_len:
            i = 0
            while i < full_len - sub_len + 1:
                j = i + sub_len - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if sub_len > max_len:
                        max_len = sub_len
                        start = i
                i += 1
            sub_len += 1

        for a in dp:
            print(a)
        return s[start:start + max_len]

print(Solution().longestPalindrome("ccc"))