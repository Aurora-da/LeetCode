class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        ans = []
        for word1 in wordsQuery:
            """
            max_len：表示目前最长公共字符串后缀的长度
            max_len_pos：表示上一个拥有最长公共后缀字符串所在的数组的位置
            max_word：用来储存上一个最长公共后缀字符串是哪一个
            """
            max_len = -1
            max_len_pos = -1
            max_word = ''

            min_len = float('inf')
            min_len_pos = -1
            for i, word in enumerate(wordsContainer):
                if len(word) < min_len:
                    min_len = len(word)
                    min_len_pos = i

            for pos, word2 in enumerate(wordsContainer):
                cur_len = 0
                for i in range(1, min(len(word2), len(word1))+1):
                    if word2[-i] != word1[-i]:
                        break
                    cur_len += 1

                if cur_len > max_len:
                    max_len = cur_len
                    max_len_pos = pos
                    max_word = word2

                if cur_len == max_len:
                    if len(max_word) > len(word2):
                        max_len_pos = pos
                        max_word = word2

            if max_len > 0:
                ans.append(max_len_pos)
            else:
                ans.append(min_len_pos)

        return ans

if __name__ == '__main__':
    s = Solution()
    wordsContainer = ["abcd", "bcd", "xbcd"]
    wordsQuery = ["cd", "bcd", "xyz"]
    print(s.stringIndices(wordsContainer, wordsQuery))