from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        toRet = []
        for word in words:
            if len(set(word)) == len(set(pattern)) and len(set(zip(word, pattern))) == len(set(word)):
                toRet.append(word)
        return toRet


print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))