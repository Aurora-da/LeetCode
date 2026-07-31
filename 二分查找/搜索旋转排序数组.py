from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        if not nums:
            return -1

        while l<=r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    s = Solution()

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    print(s.search(nums, target))