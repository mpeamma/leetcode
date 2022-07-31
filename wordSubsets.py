from typing import Counter, List

class Solution:

    def wordSubsets(self, words1, words2):
        subcounter = Counter()
        for word in words2:
            subcounter |= Counter(word)

        univerals = []
        for word in words1:
            oCounter = Counter(word)
            isUniversal = True
            for x in subcounter:
                if subcounter[x] > oCounter[x]:
                    isUniversal = False
            if isUniversal:
                univerals.append(word)
        
        return univerals


    # def isSubset(self, original, sub):
    #     for char in sub:
    #         if char in original:
    #             del original[original.index(char)]
    #         else:
    #             return False
    #     return True

    # def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    #     universals = []
    #     for str in words1:
    #         isUniveral = True
    #         for sub in words2:
    #             if not self.isSubset(list(str), sub):
    #                 isUniveral = False
    #                 break
    #         if isUniveral:
    #             universals.append(str)

    #     return universals

print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))