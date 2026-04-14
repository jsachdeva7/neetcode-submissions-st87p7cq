class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            # at any given point, either left and middle will be in sorted
            # or middle and right will be sorted
            if nums[left] > nums[middle]:
                # left and middle are not in sorted, look in left
                right = middle
            elif nums[middle] > nums[right]:
                # middle and right are not in sorted, look in right
                # middle > right, can safely skip middle
                left = middle + 1
            else:
                # everything is sorted already
                break
        return nums[left]

        