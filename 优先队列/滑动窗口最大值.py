import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # 创建优先队列默认是最小根堆，取负数是为了转换成最大根堆的问题
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i-k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([2,3,1,4,5],3))