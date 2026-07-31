class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        优化的滑动窗口法
        统计 s 的子串是否与p的字串有不同，如果存在不同即是不匹配
        """
        s_len, p_len = len(s), len(p)

        if s_len<p_len:
            return []

        ans = []
        count = [0]*26
        for i in range(p_len):
            count[ord(s[i])-97] += 1
            count[ord(p[i])-97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len-p_len):
            if count[ord(s[i])-97] == 1:
                differ -= 1
            elif count[ord(s[i])-97]==0:
                differ += 1

            count[ord(s[i])-97] -= 1

            if count[ord(s[i+p_len])-97]==-1:
                differ -= 1
            elif count[ord(s[i+p_len])-97]==0:
                differ += 1
            count[ord(s[i+p_len])-97] += 1

            if differ == 0:
                ans.append(i+1)

        return ans

if __name__ == "__main__":
    sol = Solution()
    s = ("cbaebabacd")
    p = "abc"
    ans = sol.findAnagrams(s, p)
    print(ans)


"""
滑动窗口法
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_nums = [0] * 26
        s_nums = [0] * 26

        for i in p:
            p_nums[ord(i) - 97] += 1

        ans = []
        n = len(p)
        nums = 0
        current_s = []

        for index, i in enumerate(s):
            i_index = ord(i) - 97
            if p_nums[i_index] < 1:
                s_nums = [0] * 26
                current_s = []
                nums = 0
                continue

            nums += 1
            s_nums[i_index] += 1
            current_s.append(i)

            while s_nums[i_index] > p_nums[i_index]:
                char = current_s.pop(0)
                nums -= 1
                s_nums[ord(char)-97] -= 1

            if nums == n:
                ans.append(index-n+1)
                nums -= 1
                char = current_s.pop(0)
                s_nums[ord(char)-97] -= 1

        return ans
"""