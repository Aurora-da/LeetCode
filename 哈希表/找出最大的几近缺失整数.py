from typing import List
from collections import defaultdict


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1

        res = -1
        if k == n:
            return max(nums)

        if k == 1:
            for num in nums:
                if num > res and num_dict[num] == 1:
                    res = num
            return res

        if num_dict[nums[0]] == 1:
            res = max(res, nums[0])
        if num_dict[nums[-1]] == 1:
            res = max(res, nums[-1])

        return res