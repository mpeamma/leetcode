from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idxx, x in enumerate(nums):
            for idxy, y in enumerate(nums):
                if idxx != idxy and x + y == target:
                    return [idxx, idxy]

sol = Solution()
print(sol.twoSum([1,2,3,4], 6))