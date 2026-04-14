class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # At any given point, left and mid, or mid and right will
        # be in the same sorted sublist
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
    
            if nums[left] <= nums[mid]:
                # mid and right not in same sorted sublist
                # mid and left in same sorted sublist
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # target not in sorted left->sorted sublist
                    left = mid + 1
            else:
                # mid and right are in the same sorted sublist
                if nums[mid] < target <= nums[right]:
                    # target in sorted mid->right sublist
                    left = mid + 1
                else:
                    # target not in sorted mid->right sublist
                    right = mid - 1

        return -1        