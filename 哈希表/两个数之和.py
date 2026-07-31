from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target-num], i]
            hash_map[nums[i]] = i
        return []
