from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_map = defaultdict(int)
        res = 0

        left,right = 0, 0
        n = len(s)
        while right < n:
            char_map[s[right]] += 1

            while char_map[s[right]] > 2:
                char_map[s[left]] -= 1
                left += 1

            res = max(res, right-left+1)
            right += 1

        return res