class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        count1 = s.count('1')

        zeroBlocks = []
        i = 0
        while i < n:
            start = i

            while i < n and s[i] == s[start]:
                i += 1

            if s[start] == '0':
                zeroBlocks.append(i - start)

        m = len(zeroBlocks)

        if m < 2:
            return count1

        ans = 0
        for i in range(m - 1):
            ans = max(ans, zeroBlocks[i + 1] + zeroBlocks[i])
        return count1 + ans
