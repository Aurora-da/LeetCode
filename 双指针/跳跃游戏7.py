class Solution:
    def canReach(self, s:str, minJump:int, maxJump:int) -> bool:
        n = len(s)

        if s[n-1] == "1":
            return False

        can_reach = [0] * n
        can_reach[0] = 1

        j = 1
        for i in range(n):
            if (s[i] == "0") and (can_reach[i]==1):
                # 使用这个可以确保每个j只会被遍历一次
                j = max(j, i+minJump)
                while j <= min(i + maxJump, n-1):
                    can_reach[j] = 1
                    j += 1
        return bool(can_reach[n-1])

if __name__ == '__main__':
    s = input().strip()
    minJump, maxJump = map(int, input().split())

    sol = Solution()
    if sol.canReach(s, minJump, maxJump):
        print("可以到达！")
    else:
        print("不可以到达。")