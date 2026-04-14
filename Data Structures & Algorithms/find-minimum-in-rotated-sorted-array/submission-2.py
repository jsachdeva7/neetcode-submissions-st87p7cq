class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid value is greater than the rightmost, 
            # mid and right aren't in the same sorted subarray:
            # the min is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, mid and right are in the same sorted subarray:
                # the min is in the left half
                right = mid
        
        return nums[left]