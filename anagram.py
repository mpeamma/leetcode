class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if len(s) != len(t):
            return False
        
        for ch in s:
            try:
                i = t.index(ch)
                del t[i]
            except ValueError as e:
                return False
        
        return len(t) == 0
    
    def isAnagram(self, s, t):
        sDict = {}
        tDict = {}
        for c in s:
            if c not in sDict: sDict[c] = 1
            else: sDict[c] += 1
        for c in t:
            if c not in tDict: tDict[c] = 1
            else: tDict[c] += 1
        
        return sDict == tDict

print(Solution().isAnagram(s = "anagram", t = "nagaram"))