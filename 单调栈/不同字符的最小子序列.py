class Solution:
    def smallestSubsequence(self, s: str) -> str:
        nums = {}
        for i in s:
            nums[i] = nums.get(i,0)+1

        ans = []
        visited = set()

        for ch in s:
            nums[ch] -= 1

            if ch in visited:
                continue

            while ans and ans[-1] > ch and nums[ans[-1]]>0:
                visited.remove(ans[-1])
                ans.pop()

            ans.append(ch)
            visited.add(ch)

        return ''.join(ans)

if __name__ == '__main__':
    s = input()
    sol = Solution()

    print(sol.smallestSubsequence(s))
