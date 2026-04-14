from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]  # max-heap by negating
        heapq.heapify(maxHeap)

        time = 0
        cooldown = deque()  # stores tuples of (available_time, count)

        while maxHeap or cooldown:
            time += 1

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1  # execute one task
                if count != 0:
                    cooldown.append((time + n, count))

            if cooldown and cooldown[0][0] == time:
                _, count = cooldown.popleft()
                heapq.heappush(maxHeap, count)

        return time
