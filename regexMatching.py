# class Solution:
#     def isMatch(self, s: str, r: str) -> bool:
#         if s == r:
#             return True
#         sIndex = 0
#         rIndex = 0
#         while sIndex < len(s) and rIndex < len(r):
#             if r[rIndex] == '*':
#                 if r[rIndex - 1] == "." or r[rIndex - 1] == s[sIndex]:
#                     sIndex += 1
#                 else:
#                     rIndex += 1
#             elif r[rIndex] == '.' or r[rIndex] == s[sIndex]:
#                 sIndex += 1
#                 rIndex += 1
#             else:
#                 if r[rIndex + 1] == '*':
#                     rIndex += 1
#                 else:   
#                     return False
        
#         if sIndex != len(s) :
#             return False
        
#         if rIndex != len(r) and r[len(r) - 1] != '*':
#             return False

#         return True

class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


print(Solution().isMatch("aaa", "a*a"))