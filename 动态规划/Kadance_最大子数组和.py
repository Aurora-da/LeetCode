from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float("inf")
        cur_sum =  0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            res = max(res, cur_sum)

        return res

"""
Kadane 算法
1.概述
Kadane 算法是一种用于解决最大子数组和问题的动态规划算法。
其目标是在给定的整数数组中找到一个连续的子数组，使其元素之和最大。
该算法以其简单且高效的特点广泛应用于面试和实践中。

2.算法原理
Kadane 算法的核心思想是通过迭代数组的每个元素，维护两个变量来跟踪局部最优解和全局最优解。

3.具体步骤
（1）初始化： maxEndingHere 表示在当前位置结束的最大子数组和，初始值为数组的第一个元素。 
maxSoFar 表示全局最大子数组和，初始值也为数组的第一个元素。
（2）迭代： 从数组的第二个元素开始迭代。 
对于每个元素，计算在当前位置结束的最大子数组和： maxEndingHere = max(nums[i], maxEndingHere + nums[i]) 
这表示要么继续当前子数组，要么从当前位置开始一个新的子数组。 
更新全局最大子数组和： maxSoFar = max(maxSoFar, maxEndingHere) 如果在当前位置结束的子数组和大于全局最大和，更新全局最大和。
（3）返回结果： 当迭代完成后，maxSoFar 中存储的即为最大子数组和。
"""