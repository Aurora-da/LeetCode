class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # 使用字典来记录每一个数字最近出现的位置
        num_dict = {}

        for i, num in enumerate(nums):
            if num in num_dict:
                if abs(i - num_dict[num]) <= k:
                    return True
            num_dict[num] = i
        return False

"""
力扣算法手册版：

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        nums_dict = dict()
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return True
            num_dict[num[i]] = 1
            if len(nums_dict) > k:
                del nums_dict[nums[i-k]]
        return False
"""
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    s = Solution()
    judge = s.containsNearbyDuplicate(nums, k)
    if judge:
        print("存在")
    else:
        print("不存在")