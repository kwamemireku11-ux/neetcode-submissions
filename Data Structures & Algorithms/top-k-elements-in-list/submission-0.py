class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        results = []
        for freq in range(len(nums), 0, -1):
            results.extend(buckets[freq])
            if len(results) >= k:
                break
        return results[:k]

 