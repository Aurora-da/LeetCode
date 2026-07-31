class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        l = 0
        r = len(height)-1

        max_right = -1
        max_left = -1
        while l<r:
            max_right = max(max_right, height[r])
            max_left = max(max_left, height[l])

            if height[l]<height[r]:
                ans += max_left - height[l]
                l += 1
            else:
                ans += max_right - height[r]
                r -= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    #height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4, 2, 0, 3, 2, 5]
    print(sol.trap(height))

"""
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        res = 0
        l = 0
        n = len(height)

        while l<n and height[l] < 1:
            l += 1

        while l<n:
            r = l+1
            max_right = -1
            max_right_index = -1

            while r<n:
                # 找出下一个大于等于 l 柱子的柱子的索引 r
                if height[l]<=height[r]:
                    max_right = height[r]
                    max_right_index = r
                    break
                # 找出 l 柱子后面的最高柱子
                if max_right<height[r]:
                    max_right = height[r]
                    max_right_index = r
                r += 1

            if max_right_index == -1:
                break

            min_height = min(height[l], max_right)
            for j in range(l+1, max_right_index):
                if height[j] < min_height:
                    res+=min_height-height[j]
            l = max_right_index

        return res
"""