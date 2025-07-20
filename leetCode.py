from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        n = len(matrix[0])
        heights = [0] * n  # Histogram heights untuk setiap kolom

        for row in matrix:
            for i in range(n):
                # Update histogram: bertambah jika '1', reset jika '0'
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            # Hitung area maksimum untuk histogram saat ini
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # Sentinel

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # Hapus sentinel
        return max_area
