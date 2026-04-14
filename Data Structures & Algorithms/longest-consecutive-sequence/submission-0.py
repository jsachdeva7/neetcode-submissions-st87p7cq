class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        startingSequence = []
        numberMap = {}

        # O(n)
        for i in range(len(nums)):
            if nums[i] not in numberMap:
                numberMap[nums[i]] = 1
            else:
                numberMap[nums[i]] += 1
        
        # Iterate through keys of hashmap
        maxLength = 0
        for number in numberMap:
            if number - 1 not in numberMap:
                count = 1
                nextNumber = number + 1
                while (nextNumber in numberMap):
                    count += 1
                    nextNumber += 1
                maxLength = max(maxLength, count)

        return maxLength


        


            

            

        