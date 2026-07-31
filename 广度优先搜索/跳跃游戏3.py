class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited = [False] * len(arr)
        queue = [start]

        while queue:
            pos = queue.pop(0)
            # 用于检查这个位置是否访问过，防止无限循环
            if visited[pos]:
                continue

            visited[pos] = True
            if arr[pos] == 0:
                return True

            if pos-arr[pos]>=0:
                queue.append(pos-arr[pos])
            if pos+arr[pos]<len(arr):
                queue.append(pos+arr[pos])

        return False