class Solution:
    def rob(self, nums: List[int]) -> int:
        non_adjacent_house = 0
        adjacent_house = 0

        for n in nums:
            robbed_money = max(n + non_adjacent_house, adjacent_house)
            non_adjacent_house = adjacent_house
            adjacent_house = robbed_money
        
        return robbed_money
        