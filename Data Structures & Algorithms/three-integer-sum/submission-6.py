class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums ascending so we can easily skip repeats
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                # fixed is at same number as previous
                continue
            
            fixed = i
            left = i + 1
            right = len(nums) - 1

            while left < right:
                summation = nums[fixed] + nums[left] + nums[right]
                print(summation)
                if summation == 0:
                    newTriplet = [nums[fixed], nums[left], nums[right]]
                    triplets.append(newTriplet)
                    while left < right and nums[left] == nums[left + 1]:
                        # next element is the same, move along
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        # previous element is the same, move along
                        right = right - 1
                    left += 1
                    right -= 1
                elif summation < 0:
                    # normalize sum to be higher
                    left = left + 1
                else:
                    # normalize sum to be lower
                    right = right - 1
                
        return triplets