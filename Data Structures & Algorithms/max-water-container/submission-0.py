class Solution:
    def getArea(self, heights, li, ri):
        return min(heights[li], heights[ri])*abs(ri-li)
    def maxArea(self, heights: List[int]) -> int:
        maxv = 0
        l = 0
        r = len(heights)-1
        while l < r:
            if self.getArea(heights, l, r) > maxv: maxv = self.getArea(heights, l, r)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxv




