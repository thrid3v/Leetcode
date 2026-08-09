class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h,j = stack.pop()
                w = i - j
                max_area = max(max_area, w*h)
                start = j
            stack.append((height,start))
        
        while stack:
            h,j = stack.pop()
            w = n - j
            max_area = max(max_area, w*h)

        return max_area