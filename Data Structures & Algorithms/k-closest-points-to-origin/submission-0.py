class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        for point in points:
            xi = point[0]
            yi = point[1]
            distance = (xi**2 + yi**2)**0.5
            if distance not in distances:
                distances[distance] = [point]
            else:
                distances[distance].append(point)
        
        minHeap = []
        for distance in distances:
            heapq.heappush(minHeap, distance)
        
        # How to pop out the smallest distance first
        appended = 0
        result = []
        while appended < k and len(minHeap) > 0:
            smallest = heapq.heappop(minHeap)
            for point in distances[smallest]:
                if appended < k:
                    result.append(point)
                    appended += 1
                else:
                    return result

        return result

            


