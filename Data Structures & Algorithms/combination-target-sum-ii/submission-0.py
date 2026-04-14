class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, combo: List[int], curSum: int):
            if curSum == target:
                res.append(combo.copy())
                return
            if curSum > target or i >= len(candidates):
                return

            # include candidates[i]
            combo.append(candidates[i])
            dfs(i + 1, combo, curSum + candidates[i])
            combo.pop()

            # skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, combo, curSum)

        dfs(0, [], 0)
        return res
            
            
        