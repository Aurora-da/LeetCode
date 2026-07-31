class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return -1

        str_nums = dict()
        n = len(s)
        current_str = []
        max_len = -1

        for i in range(n):
            if s[i] not in str_nums:
                str_nums[s[i]] = 0
            str_nums[s[i]] += 1
            current_str.append(s[i])

            while str_nums[s[i]] > 1:
                if current_str == []:
                    break
                char = current_str.pop(0)
                str_nums[char] -= 1
            max_len = max(max_len, len(current_str))

        return max_len

if __name__ == '__main__':
    sol = Solution()
    #s = "abcabcbb"
    #s = "abcabcbb"
    #s = "bbbbb"
    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))
