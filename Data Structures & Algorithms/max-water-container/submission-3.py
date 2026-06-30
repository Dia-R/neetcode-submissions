class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        output = 0

        while l != r:
            curWidth = r-l
            maxWater = min(heights[l], heights[r])*curWidth
            print([heights[l], heights[r], curWidth, maxWater,output])
            output = max(output, maxWater)

            if heights[l]<heights[r]:
                l += 1
            else:
                r -= 1
        
        return output
            



        
        

        