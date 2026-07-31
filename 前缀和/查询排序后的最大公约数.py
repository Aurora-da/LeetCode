from bisect import bisect_left
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt = [0] * (mx + 1)

        for num in nums:
            cnt[num] += 1

        for i in range(1, mx + 1):
            for j in range(2 * i, mx + 1, i):
                cnt[i] += cnt[j]

        for i in range(1, mx + 1):
            cnt[i] = cnt[i] * (cnt[i] - 1) // 2

        for i in range(mx, 0, -1):
            for j in range(i * 2, mx + 1, i):
                cnt[i] -= cnt[j]

        # 前缀和
        for i in range(1, mx + 1):
            cnt[i] += cnt[i - 1]

        ans = []

        for q in queries:
            q += 1
            pos = bisect_left(cnt, q)
            ans.append(pos)

        return ans