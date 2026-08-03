from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        suffix_sum = [0]*(n-1) + [stoneValue[-1]]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = stoneValue[i] + suffix_sum[i+1]

        f = [0]*(n+1)
        for i in range(n-1, -1, -1):
            """
            1.如果拿 1 堆：
            他拿走了 stoneValue[i]，剩下的石子是 i+1 到末尾。
            此时对手变成了“先手”，对手在剩余石子中最多能拿 f[i+1] 分。
            当前玩家最终总分 = suffix_sum[i] - f[i+1]（因为总分减去对手拿走的，剩下的就是自己的）。
            
            2.如果拿 2 堆：
            同理，当前玩家最终总分 = suffix_sum[i] - f[i+2]。
            
            3.如果拿 3 堆：
            同理，当前玩家最终总分 = suffix_sum[i] - f[i+3]。
            """
            f[i] = suffix_sum[i] - min(f[i+1:i+4])

        if f[0]*2==suffix_sum[0]:
            return "Tie"
        else:
            return "Alice" if f[0]*2>suffix_sum[0] else "Bob"