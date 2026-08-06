from asyncio import start_server
from typing import List

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a%b
    return a

class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        """旋转数组"""
        n = len(nums)
        k = k%n

        # 计算出有多少个环，代表要进行几次循环
        count = gcd(k, n)
        for i in range(count):
            current = i
            # 首先保存第一个元素，方便后续进行元素交换
            prev = nums[i]
            while True:
                # 求出 prev 元素交换后的位置
                next = (current+k)%n
                nums[next], prev = prev, nums[next]
                current = next
                # 当前的位置等于初始位置时表示已经全部找到交换后的所在位置，本次交换结束
                if current == i:
                    break


"""
自己想的：切片
class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        k = k%n

        nums[:] = nums[n-k:n]+nums[:k-1]
"""