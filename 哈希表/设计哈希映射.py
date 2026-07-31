class MyHashMap:
    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        # 要先检查key是否已经存在了
        for i, kv in enumerate(self.data):
            if kv[0] == key:
                self.data[i][1] = value
                return

        # 不存在的话则就新增这个数据
        self.data.append([key, value])

    def get(self, key: int) -> int:
        for kv in self.data:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        for i, kv in enumerate(self.data):
            if kv[0] == key:
                del self.data[i]
                return

if __name__ == "__main__":
    hash_map = MyHashMap()