class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Get the coordinates of the first two points
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        # Check the slope between the first two points
        # Use a small epsilon value for floating-point comparisons
        epsilon = 1e-8
        slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')
        
        # Check the slope between the remaining points
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            current_slope = (y - y1) / (x - x1) if (x - x1) != 0 else float('inf')
            
            # Compare the slopes
            if abs(current_slope - slope) > epsilon:
                return False
        
        return True