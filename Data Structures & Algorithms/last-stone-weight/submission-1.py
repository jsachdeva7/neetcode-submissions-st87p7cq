class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) >= 2:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            # means y is bigger than x
            if x != y:
                y = y - x
                heapq.heappush(maxHeap, -y)
        
        if len(maxHeap) == 0:
            return 0
        return -maxHeap[0]
                
