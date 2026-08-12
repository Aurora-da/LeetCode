from typing import List

class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # 记录第一行是否存在0
        first_row_has_zero = 0 in matrix[0]
        # 记录第一列是否存在0
        first_col_has_zero = any(row[0]==0 for row in matrix)

        # 用第一列 matrix[i][0] 保存 row_has_zero[i]
        # 用第一行 matrix[0][j] 保存 col_has_zero[j]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # 开始遍历，如果该元素所在的行或者列中存在0元素，则就将这个位置的元素变为0
        # 从1开始是为了跳过第一行，将第一行留到最后修改
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0

        # 如果第一列有0，则将第一列的所有元素全部变为0
        if first_col_has_zero:
            for row in matrix:
                row[0] = 0

        # 如果第一行有0，则将第一行的元素全部变为0
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

"""
class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        # 用来储存数组中元素为零的元素位置
        idx_zero = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    idx_zero.append([i, j])

        # 依次遍历所有为0的矩阵的位置，然后将所在的行列全部标记为0
        for i, j in idx_zero:
            for idx in range(n):
                matrix[idx][j] = 0
            for idx in range(m):
                matrix[i][idx] = 0
"""