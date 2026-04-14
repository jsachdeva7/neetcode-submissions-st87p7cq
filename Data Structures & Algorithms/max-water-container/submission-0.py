class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            leftHeight = heights[left]
            rightHeight = heights[right]
            width = right - left
            height = min(leftHeight, rightHeight)
            water = width * height
            maxWater = max(maxWater, water)

            if leftHeight <= rightHeight:
                left = left + 1
            else:
                right = right - 1
        
        return maxWater