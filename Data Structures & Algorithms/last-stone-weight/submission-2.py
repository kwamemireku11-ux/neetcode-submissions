class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            new_stone = stone1 - stone2
            if new_stone > 0:
                heapq.heappush(heap, -new_stone)
        if not heap:
            return 0
        else:
            return -heap[0]



        