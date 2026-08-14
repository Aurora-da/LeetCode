from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        # 先进行水平翻转，将上面的元素与下面的元素进行互换
        for i in range(n//2):
            for j in range(m):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

        # 然后进行对角线置换，沿着对角线对对称的元素进行互换得到结果
        for i in range(n):
            for j in range(i+1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]