from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_num = defaultdict(int)
        for i in t:
            t_num[i] += 1

        s_num = defaultdict(int)
        t_set = set(t)
        cur_num = 0
        left = 0
        res = ""
        m = len(t)
        min_len = float("inf")

        for right, c in enumerate(s):
            if c in t_set:
                s_num[c] += 1
                if s_num[c]<=t_num[c]:
                    cur_num += 1

            while cur_num == m:
                window_len = right-left+1
                # 最新满足条件的子串比最优子串长度低时：更新结果
                if window_len<min_len:
                    min_len = window_len
                    res = s[left:right+1]

                left_char = s[left]
                if left_char in t_set:
                    s_num[left_char] -= 1
                    if s_num[left_char]<t_num[left_char]:
                        cur_num-=1
                left += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s, t))