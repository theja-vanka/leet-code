class Solution:
    def rob(self, nums: List[int]) -> int:
        non_adj = 0
        adj = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i]+ non_adj, adj)
            non_adj = adj
            adj = curr
        
        return adj
        