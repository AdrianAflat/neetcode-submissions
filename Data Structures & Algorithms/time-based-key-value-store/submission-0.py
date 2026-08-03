class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        values = self.store.get(key, [])
        print(values)
        
        l = 0
        r = len(values) -1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                l = m + 1
                result = values[m][0]
            else:
                r = m - 1

        return result