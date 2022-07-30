from typing import List

class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     i = 0
    #     max_area = 0
    #     while i < len(height):
    #         j = i+1
    #         while j < len(height):
    #             area = min(height[i], height[j]) * (j - i)
    #             if area > max_area:
    #                 max_area = area
    #             j += 1
    #         i += 1
    #     return max_area
    def maxArea(self, height):
        i = 0
        j = len(height)- 1
        max_area = 0
        while i < j:
            current_height = min(height[i], height[j])
            max_area = max(max_area, current_height * (j - i))
            while height[i] <= current_height and i < j: i += 1
            while height[j] <= current_height and i < j: j -= 1
        
        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))