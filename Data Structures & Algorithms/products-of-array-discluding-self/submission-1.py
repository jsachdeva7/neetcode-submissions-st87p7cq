class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        numZeroes = 0
        for num in nums:
            if num == 0:
                numZeroes += 1
            else:
                product *= num

        result = []
        for num in nums:
            if (numZeroes == 1 and not num == 0) or numZeroes > 1:
                result.append(0)
            elif numZeroes == 1:
                # 0
                result.append(product)
            else:
                result.append(int(product / num))
        
        return result

        