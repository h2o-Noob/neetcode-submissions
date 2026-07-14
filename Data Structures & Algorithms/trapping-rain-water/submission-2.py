class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        rMax = [] * len(height)
        lMax = [] * len(height)
        rCurr = 0
        lCurr = 0
        area = 0

        for i in height:
            rCurr = max(rCurr, i)
            rMax.append(rCurr)
        
        for i in reversed(height):
            lCurr = max(lCurr, i)
            lMax.append(lCurr)
        
        lMax.reverse()

        for j, i in enumerate(height):
            if i < min(rMax[j], lMax[j]):
                area += min(rMax[j], lMax[j]) - i
        
        return area
        
        

