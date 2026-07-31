"""
核心技巧
    1. 位掩码（Bitmask）：
    (1)因为数组元素范围是 1 到 n, 1 << A[i] 将第 A[i] 位设为 1
    (2)例如：A[0]=3 → 1<<3 = 二进制 1000（第3位是1）

    2. p 和 q：
    (1)p：A 中到当前位置所有出现过的数字的位掩码
    (2)q：B 中到当前位置所有出现过的数字的位掩码

    3. p & q：
    (1)按位与，得到同时在 A 和 B 前缀中出现过的数字的位掩码
    (2).bit_count() 返回二进制中 1 的个数，就是共同出现的数字个数
"""

class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        p = q = 0
        ans = [0] * len(A)
        for i in range(len(A)):
            p |= 1 << A[i]
            q |= 1 << B[i]
            ans[i] = (p&q).bit_count()
        return ans