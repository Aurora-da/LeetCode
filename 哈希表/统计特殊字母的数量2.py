class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        w = dict()
        for pos, char in enumerate(word):
            if char.islower():
                w[char] = pos
            else:
                if char not in w:
                    w[char] = pos

        num = 0
        for i in range(ord('a'), ord('z') + 1):
            char = chr(i)

            if char not in w or char.upper() not in w:
                continue

            if w[char] < w[char.upper()]:
                num += 1

        return num

if __name__ == "__main__":
    s = Solution()
    word = input()
    print(s.numberOfSpecialChars(word))