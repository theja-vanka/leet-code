class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        ball_to_color: dict = {}
        color_counter: dict = {}
        result: list = []

        for q in queries:
            ball, color = q[0], q[1]

            if ball in ball_to_color:
                old_color = ball_to_color[ball]
                color_counter[old_color] -= 1
                if color_counter[old_color] == 0:
                    del color_counter[old_color]
            
            if color not in color_counter:
                color_counter[color] = 0
            color_counter[color] += 1
            ball_to_color[ball] = color

            result.append(len(color_counter.keys()))
        return result