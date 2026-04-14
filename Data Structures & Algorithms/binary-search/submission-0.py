class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            middle_val = nums[middle]
            if target == middle_val:
                return middle
            elif target > middle_val:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1
        