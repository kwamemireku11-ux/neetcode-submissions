class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        result = len(nums) + 1
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result != len(nums) + 1 else 0
    

        


    
        