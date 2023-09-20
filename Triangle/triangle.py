def minimumTotal(triangle):
    # Copy the last row as the initial result
    result = list(triangle[-1])
    
    # Start from the second last row and work upwards
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            # For each element, find the minimum of the two adjacent elements in the next row and add it to the current element
            result[j] = triangle[i][j] + min(result[j], result[j+1])
    
    return result[0]  # The first element will contain the minimum path sum
