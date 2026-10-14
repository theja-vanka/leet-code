class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result = []

        def summation(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            
            if i>=len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            summation(i, curr, total + candidates[i])
            curr.pop()
            summation(i + 1, curr, total)

        summation(0, [], 0)
        return result