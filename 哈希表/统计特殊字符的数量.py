class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        letter_lower = set()
        letter_upper = set()
        for char in word:
            if 'a' <= char <= 'z':
                letter_lower.add(char)
            else:
                letter_upper.add(char)

        for char in letter_lower:
            if char.upper() in letter_upper:
                count += 1

        return count

if __name__ == "__main__":
    s = Solution()
    word = input()
    print(s.numberOfSpecialChars(word))