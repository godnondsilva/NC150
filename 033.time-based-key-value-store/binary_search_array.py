class TimeMap:

    def __init__(self):
        self.mpp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key in self.mpp):
            self.mpp[key].append([timestamp, value])
        else:
            self.mpp[key]=[[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        value_array = self.mpp.get(key, [])
        if not value_array:
            return ""

        l,r=0,len(value_array)-1
        result = -1

        while l<=r:
            m = l + (r - l) // 2
            if value_array[m][0] <= timestamp:
                result = m
                l = m + 1
            else:
                r = m - 1
        return value_array[result][1] if result != -1 else ""