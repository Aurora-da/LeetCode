from typing import List

class Solution:
    def intersection(self, nums1: List[int], num2: List[int]) -> List[int]:
        nums_set = set()
        for num in nums1:
            if num not in nums_set:
                nums_set.add(num)

        ans = set()
        for num in num2:
            if num in nums_set:
                ans.add(num)

        return list(ans)

if __name__ == '__main__':
    s = Solution()
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    ans = s.intersection(nums1, nums2)
    print(ans)