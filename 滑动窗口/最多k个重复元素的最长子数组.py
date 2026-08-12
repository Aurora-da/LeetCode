from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """双指针 + 滑动窗口 + 字典"""
        res = 0
        left = 0
        num_dict = defaultdict(int)

        for right, x in enumerate(nums):
            num_dict[x] += 1
            while num_dict[x] > k:
                num_dict[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, input().split()))
    k = int(input())


"""
自己写的：滑动窗口 + 哈希表
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        num_dict = defaultdict(int)
        res = -1
        now_len = 0
        now = []

        for num in nums:
            num_dict[num] += 1
            now_len += 1
            now.append(num)

            while num_dict[num] > k:
                now_num = now.pop(0)
                num_dict[now_num] -= 1
                now_len -= 1

            res = max(res, now_len)

        return res
"""