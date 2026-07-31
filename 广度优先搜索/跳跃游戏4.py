from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        # defaultdict可以为不存在的键提供一个默认值，而不需要显示检查键是否存在
        data = defaultdict(list)
        for i, a in enumerate(arr):
            data[a].append(i)
        visited = set()
        # deque是一个双端队列
        q = deque()
        q.append([0, 0])
        visited.add(0)
        while q:
            pos, steps = q.popleft()
            if pos == len(arr)-1:
                return steps
            now = arr[pos]
            steps += 1
            for i in data[now]:
                if i not in visited:
                    visited.add(i)
                    q.append([i, steps])
            del data[now]
            if pos+1 < len(arr) and (pos+1) not in visited:
                visited.add(pos+1)
                q.append([pos+1, steps])
            if pos-1 >= 0 and (pos-1) not in visited:
                visited.add(pos-1)
                q.append([pos-1, steps])

if __name__ == "__main__":
    pass