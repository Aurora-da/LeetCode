class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        data = set()
        max_num = 0
        for num in arr1:
            while num > 0:
                data.add(num)
                num = num // 10

        for num in arr2:
            while num > 0:
                if num in data:
                    max_num = max(max_num, num)
                num = num // 10

        return 0 if max_num == 0 else len(str(max_num))

if __name__ == "__main__":
    arr1 = [1, 10, 100]
    arr2 = [1000]
    s = Solution()
    print(s.longestCommonPrefix(arr1, arr2))