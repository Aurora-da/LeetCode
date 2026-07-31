class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)):
            if i == 1:
                dp.append(max(nums[i], nums[i-1]))
            else:
                cur_max = max(dp[i-1], dp[i-2]+nums[i])
                dp.append(cur_max)
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    nums = list(map(int, input().split()))
    print(s.rob(nums))