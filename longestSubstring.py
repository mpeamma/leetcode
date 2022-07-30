class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        longest = ""
        
        for start in range(len(s)):
            for stop in range(start, len(s)):
                sub = s[start:stop + 1]
                if len(sub) > 1 and s[stop] in sub[0:len(sub) - 1]:
                    break
                longest = sub if len(sub) > length else longest
                length = len(sub) if len(sub) > length else length
                
        return length

sol = Solution()
print(sol.lengthOfLongestSubstring("aabcbd"))