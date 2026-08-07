from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """哈希表"""
        n = len(nums)
        # 首先将所有的负数转换为正数
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # 开始标记，将存在的数字 i 所对应得数组下标 i-1 标记为负数，表示这个数存在数组中
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # 寻找符合条件的结果，如果为正数，表示不存在于原数组，即返回结果即可
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

