class Solution:
    def rob(self, nums: list[int]) -> int:
        num1 = num2 = 0
        for num in nums:
            num1, num2 = num2, max(num2, num+num1)
        return num2

if __name__ == "__main__":
    s = Solution()
    nums = list(map(int, input().split()))
    print(s.rob(nums))