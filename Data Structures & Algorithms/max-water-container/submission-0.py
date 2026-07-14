class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0

        i = 0
        j = len(heights) - 1

        while i < j:
            area = max(min(heights[i], heights[j]) * (j - i), area)

            if heights[i] > heights[j]:
                j -= 1

            else:
                i += 1
        return area
            
