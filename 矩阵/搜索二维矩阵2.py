import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            # bisect_left是返回第一个小于等于target元素的下标
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True

        return False