import argparse

def star_pyramid(n):
    for row in range(1, n+1):#calc the rows
        start_index=(n-row)#calc the amount of spaces preceding asterisks
        print (" "*start_index, end='')
        for star in range(row + row-1):# calc amount of iterations
            if star %2 ==0:#even iteration = asterisks
                print("#",end='')
            else:
                print(" ",end='')#odd iteration = space
        print("")

star_pyramid(7)