class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for x, y in points:
            dist = (x**2 + y**2)
            heapq.heappush(heap, [dist, [x, y]])
        for num in range(k):
            result.append(heapq.heappop(heap)[1])
        return result




            

        