from typing import List

class Solution:
    def __init__(self, n):
        self.n = n
        self.arr = []

    def set_arr(self) -> None:
        self.arr = list(map(int, input("请输入数组中的元素（输入用空格进行分隔，输入回车表示结束）：").split()))

    def get_arr(self) -> List[int]:
        return self.arr

    def arrayRankTransform(self) -> List[int]:
        # 去重排序
        sorted_arr = sorted(set(self.arr))

        # 构建哈希表
        num_dict = {num : index  for index, num in enumerate(sorted_arr, 1)}

        # 构建结果数组
        ans = []
        for i in self.arr:
            ans.append(num_dict.get(i))
        return ans

    def get_ans(self):
        return self.arrayRankTransform()

if __name__ == '__main__':
    n = int(input())

    sol = Solution(n)
    sol.set_arr()

    ans = sol.get_ans()
    for i in ans:
        print(i, end=" ")


"""
import copy
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_dict = dict()
        copy_arr = copy.deepcopy(arr)
        copy_arr.sort()

        index = 0
        for i in copy_arr:
            if num_dict.get(i) is None:
                num_dict[i] = index
                index += 1

        for i in arr:
            print(num_dict.get(i)+1, end=" ")

if __name__ == '__main__':
    sol = Solution()

    arr = [40, 10, 20, 30]
    sol.arrayRankTransform(arr)
"""