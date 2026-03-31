class Solution:
    def maxArea(self, height: List[int]) -> int:

        left: int = 0
        right: int = len(height) - 1

        area: int = 0
        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
            