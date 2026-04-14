import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1

            if x > y:
                heapq.heappush(stones, (x - y) * -1)
            elif x < y:
                heapq.heappush(stones, (y - x) * -1)

        return stones[0] * -1 if len(stones) == 1 else 0