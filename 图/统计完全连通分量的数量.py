from typing import List

class Solution:
    def countCompleteComponents(self, n:int, edges:List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = set()
        stack = []

        ans = 0
        for i in range(n):
            if i in visited:
                continue

            # k 表示当前连通分量的节点数
            k = 0
            # v 表示当前连通分量的边数
            v = 0
            stack.append(i)
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                k += 1
                v += len(graph[node])
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            if v == k*(k-1):
                ans += 1

        return ans

if __name__ == '__main__':
    n = int(input())
    edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]

    sol = Solution()
    ans = sol.countCompleteComponents(n, edges)
    print(ans)
