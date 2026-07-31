class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 为每一列都创建一个检查的集合
        col = [set() for _ in range(9)]
        # 为每一个9宫格创建一个检查的集合
        row_col = [[set() for _ in range(3)] for _ in range(3)]
        i = 0
        for row in board:
            # 用来检查每一行是否有重复的数字
            row_judge = set()
            for num in range(len(row)):
                # 遇到空格直接跳过继续检查
                if row[num] == '.':
                    continue

                if row[num] in row_judge:
                    return False
                else:
                    row_judge.add(row[num])

                # 用来检查每一列是否有重复的数字
                if row[num] in col[num]:
                    return False
                else:
                    col[num].add(row[num])

                # 用来检查9宫格中是否有重复的数字
                if row[num] in row_col[i//3][num//3]:
                    return False
                else:
                    row_col[i//3][num//3].add(row[num])
            i += 1

        return True

if __name__ == "__main__":
    board = [input().split() for _ in range(9)]
    s = Solution()
    print(s.isValidSudoku(board))