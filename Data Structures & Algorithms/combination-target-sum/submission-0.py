class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, combo: List[int], curSum: int):
            curSum = sum(combo)
            if curSum == target:
                res.append(combo.copy())
                return
            if i >= len(nums) or curSum > target:
                return
            
            # include candidate
            combo.append(nums[i])
            dfs(i, combo, curSum + nums[i])

            # don't include candidate
            combo.pop()
            dfs(i + 1, combo, curSum)

        dfs(0, [], 0)
        return res
            

        