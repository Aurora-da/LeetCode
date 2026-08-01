import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            # 构造一个递减的单调队列，保证所有可能的结果都在队列中
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            # 如果新元素大于队列后面的那些，则说明那些元素不是这段区间的最大值，直接弹出即可
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            # 将新元素的下标放入队列中
            q.append(i)
            # 将不在区间的元素全部弹出
            while q[0]<=i-k:
                q.popleft()
            # 队列的首个下标就是当前区间的最大值
            ans.append(nums[q[0]])

        return ans