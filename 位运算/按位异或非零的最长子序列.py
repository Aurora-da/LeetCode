from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor_res = 0

        for num in nums:
            xor_res ^= num

        if xor_res != 0:
            return n

        for num in nums:
            if num != 0:
                return n - 1

        return 0
