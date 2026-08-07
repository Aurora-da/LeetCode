from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """前缀积后缀积法"""
        n = len(nums)
        res = [0] * n

        res[0] = 1
        for i in range(1, n):
            res[i] = res[i-1]*nums[i-1]

        r = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i]*r
            r *= nums[i]

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.productExceptSelf(nums))


"""
方法一：定义两个数组分别表示某个位置的左右两侧的乘积，随后依次相乘得到结果
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n

        # 存放 i 左侧的乘积
        temp = 1
        for i in range(1, n):
            temp = temp * nums[i-1]
            left[i] = temp

        # 存放 i 右侧的乘积
        temp = 1
        for i in range(n-2, -1, -1):
            temp = temp * nums[i+1]
            right[i] = temp

        # 依次相乘得最终结果
        res = [right[0]]
        for i in range(1, n-1):
            res.append(left[i] * right[i])
        res.append(left[n-1])

        return res

"""
