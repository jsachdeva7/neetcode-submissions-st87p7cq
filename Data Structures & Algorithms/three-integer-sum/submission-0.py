class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        # Sort nums
        nums.sort()
        
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            fixed = i
            left, right = i + 1, len(nums) - 1
            while left < right:
                summation = nums[left] + nums[fixed] + nums[right]
                if summation == 0:
                    triplet = [nums[fixed], nums[left], nums[right]]
                    results.append(triplet)
                    left += 1
                    right -= 1
                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif summation < 0:
                    left += 1
                else:
                    right -= 1
        
        return results 