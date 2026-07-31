from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 去除重复元素
        nums = set(nums)

        # 从0开始计数，防止存在空序列的情况
        max_len = 0
        for num in nums:
            # 如果这个数的前一个数在元组中，说明已经统计过，直接跳过
            if num-1 not in nums:
                now_len = 1

                while num+1 in nums:
                    now_len += 1
                    num += 1

                max_len = max(max_len, now_len)

        return max_len