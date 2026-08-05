from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # 优化用 deque 代替 list 作为队列
        # 建立图
        fun_graph = [[] for _ in range(n+1)]
        for a, b in invocations:
            fun_graph[a].append(b)

        # 用来存储所有的可疑方法
        suspect = set()
        # 存储当前所在的节点
        queue = deque([k])
        while queue:
            node = queue.popleft()
            if node in suspect:
                continue
            suspect.add(node)
            for neighbor in fun_graph[node]:
                if neighbor not in suspect:
                    queue.append(neighbor)

        for i in range(n):
            if i not in suspect:
                for j in fun_graph[i]:
                    if j in suspect:
                        return list(range(n))

        return [_ for _ in range(n) if _ not in suspect]

"""
自己想出来的方法：图 + 广度优先搜索 + 哈希
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # 建立图
        fun_graph = [[] for _ in range(n)]
        for a, b in invocations:
            fun_graph[a].append(b)

        # 用来存储所有的可疑方法
        suspect = set()
        # 存储当前所在的节点
        remaining = [k]
        while remaining:
            node = remaining.pop(0)
            if node in suspect:
                continue
            suspect.add(node)
            for neighbor in fun_graph[node]:
                if neighbor not in suspect:
                    remaining.append(neighbor)

        for i in range(n):
            if i not in suspect:
                for j in fun_graph[i]:
                    if j in suspect:
                        return list(range(n))

        return [_ for _ in range(n) if _ not in suspect]
"""