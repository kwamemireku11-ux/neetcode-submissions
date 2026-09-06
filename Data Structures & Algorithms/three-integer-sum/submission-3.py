class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        clean = sorted(nums)
        stored_triplets = []
        
        for i in range(len(clean) - 2):
            if i > 0 and clean[i] == clean[i-1]:
                continue
            left = i + 1
            right = len(clean) - 1
            while left < right:
                if clean[left] + clean[right] < -clean[i]:
                    left += 1
                elif clean[left] + clean[right] > -clean[i]:
                    right -= 1
                else:
                    stored_triplets.append([clean[i], clean[left], clean[right]])
                    left += 1
                    right -= 1
                    while left < right and clean[left] == clean[left - 1]:
                        left += 1
                    while left < right and clean[right] == clean[right + 1]:
                        right -= 1

        return stored_triplets

























            



        