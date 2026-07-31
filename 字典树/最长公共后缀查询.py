class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        # 构建后缀字典树
        root = TrieNode()

        # 插入每一个字符串
        for i, word in enumerate(wordsContainer):
            node = root
            # 反转字符串，变成前缀问题
            reversed_word = word[::-1]

            # 更新根节点为所有字符串中最短长度的索引
            if root.best_idx == -1 or len(word) < len(wordsContainer[root.best_idx]):
                root.best_idx = i

            for j, ch in enumerate(reversed_word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

                if node.best_idx == -1 or len(word) < len(wordsContainer[node.best_idx]):
                    node.best_idx = i

        ans = []
        for query in wordsQuery:
            node = root
            reversed_query = query[::-1]

            # 沿着字典树走，直到走不下去
            for ch in reversed_query:
                if ch in node.children:
                    node = node.children[ch]
                else:
                    break

            ans.append(node.best_idx)

        return ans

if __name__ == "__main__":
    s = Solution()
    wordsContainer = ["abcd", "bcd", "xbcd"]
    wordsQuery = ["cd", "bcd", "xyz"]
    print(s.stringIndices(wordsContainer, wordsQuery))