from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 表示某一个前缀和出现的次数
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        # 当前前缀和
        cur_sum = 0
        ans = 0

        for num in nums:
            cur_sum += num

            """
            pre[r+1] - pre[l] = k 
            转换成
            pre[l] = pre[r+1] - k
            """
            ans += prefix_count[cur_sum-k]
            prefix_count[cur_sum] += 1
        return ans