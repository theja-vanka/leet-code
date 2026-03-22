class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        ball_to_color: dict = {}
        color_counter: dict = {}
        result: list = []

        for ball, color in queries:
            if ball in ball_to_color and ball_to_color[ball] in color_counter:
                color_counter[ball_to_color[ball]] -= 1
                if color_counter[ball_to_color[ball]] == 0:
                    del color_counter[ball_to_color[ball]]
            
            ball_to_color[ball] = color
            color_counter[color] = color_counter.get(color, 0) + 1          

            result.append(len(color_counter.keys()))
        return result