class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [[timestamp, value]]
        else:
            self.timeMap[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        values = self.timeMap[key]

        left = 0
        right = len(values) - 1
        res = ""

        while left <= right:
            middle = (left + right) // 2
            middle_value = values[middle]
            if (middle_value[0] == timestamp):
                return values[middle][1]
            elif (middle_value[0] < timestamp):
                res = middle_value[1]
                left = middle + 1
            else:
                right = middle - 1
        return res
