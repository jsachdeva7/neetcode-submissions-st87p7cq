class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for num in nums:
            if num in hashtable: # this checks if there's a key in the hashtable equal to num
                return True
            # In the event that key doesn't exist yet
            hashtable[num] = True
        return False
        