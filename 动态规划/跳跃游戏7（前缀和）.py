class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # f[i] = 1表示这个地方可以到达, f[i]=0表示无法到达, pre用来储存这个节点之前有多少个“0”节点
        f, pre = [0]*n, [0]*n

        f[0] = 1
        # 初始化这个范围的数组，0到minJump-1这个范围有0这个点是可以到达的
        for i in range(minJump):
            pre[i] = 1

        for i in range(minJump, n):
            l, r = i-maxJump, i-minJump
            if s[i] == "0":
                total = pre[r] - (0 if l<=0 else pre[l-1])
                f[i] = int(total!=0)
            pre[i] = pre[i-1] +f[i]

        return bool(f[n-1])

if __name__ == "__main__":
    s = input().strip()
    minJump, maxJump = map(int, input().split())

    sol = Solution()
    if sol.canReach(s, minJump, maxJump):
        print("可以到达！")
    else:
        print("不可以到达。")
