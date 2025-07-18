class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0, len(height) -1
        maxarea = 0
        while left < right:
            
            width = right - left
            height1 = min(height[left], height[right])
            total_area = width * height1
            if int(total_area) > maxarea:
                maxarea = total_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxarea
