from typing import List
from math import log2

class Solution:
    def grayCodeFirst(self, n: int) -> List[int]:
        ret = [];
        ret.append(0);
        runningIndex = 0;
        loopAttempts = 0;
        while len(ret) < 2 ** n and loopAttempts < 2:
            for x in range(2 ** n):
                stringVal = ('{0:b}'.format(x ^ ret[runningIndex]))
                if stringVal.count("1") == 1 and x not in ret:
                    runningIndex += 1
                    ret.append(x)
                    loopAttempts = 0
            loopAttempts += 1
        return ret;

    def grayCode(self, n: int) -> List[int]:
        return [0] + self.dfs(0, range(1, 2 ** n))

    def dfs(self, current, options):
        if len(options) == 1:
            if log2(options[0]).is_integer():  
                return [options[0]]
            else:
                raise Exception("Final number doesn't satisfy")

        for option in options:
            stringVal = ('{0:b}'.format(current ^ option))
            if stringVal.count("1") == 1:
                filteredOptions = list(options)
                filteredOptions.remove(option)
                try:
                    return [option] + self.dfs(option, filteredOptions)
                except:
                    pass

        raise Exception("No possible way out")

sol = Solution()
print(sol.grayCode(5))