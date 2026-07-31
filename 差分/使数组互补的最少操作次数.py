class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        op = [0] * (2*limit+2)

        for i in range(n//2):
            min_num = min(nums[i], nums[n-i-1])
            max_num = max(nums[i], nums[n-i-1])

            op[2] += 2
            op[min_num+1] -= 1
            op[min_num+max_num] -= 1
            op[max_num+min_num+1] += 1
            op[max_num+limit+1] += 1

        min_ops = n
        cur_ops = 0
        for i in range(2, 2*limit+1):
            cur_ops += op[i]
            if cur_ops < min_ops:
                min_ops = cur_ops

        return min_ops

if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, input().split()))
    limit = int(input())

    print(sol.minMoves(nums, limit))