class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        numZeroes = 0
        for num in nums:
            if num == 0:
                numZeroes += 1
            else:
                product *= num

        if numZeroes > 1:
            return [0] * len(nums)

        result = []
        for num in nums:
            if numZeroes == 1 and not num == 0:
                result.append(0)
            elif numZeroes == 1:
                result.append(product)
            else:
                result.append(int(product / num))
        
        return result