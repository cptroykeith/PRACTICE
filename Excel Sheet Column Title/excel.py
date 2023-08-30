def convertToTitle(columnNumber):
    title = ""
    
    while columnNumber > 0:
        # Convert the remainder into the corresponding letter
        remainder = (columnNumber - 1) % 26
        title = chr(65 + remainder) + title
        
        # Update columnNumber to move to the next division
        columnNumber = (columnNumber - 1) // 26
    
    return title


