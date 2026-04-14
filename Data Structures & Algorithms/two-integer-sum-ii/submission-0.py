class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            left_num = numbers[left]
            right_num = numbers[right]
            sum = left_num + right_num

            if sum == target: 
                return [left + 1, right + 1]
            elif sum <= target:
                left = left + 1
            elif sum >= target:
                right = right - 1
        
        return []
            
        