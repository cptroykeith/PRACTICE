import argparse

def right_pyramid(n):
    for row in range(1, n+1):
        start_index=(n-row)
        print(" "*start_index, end='')
        for star in range(row):
            print("#", end='')

        print("")

right_pyramid(7)

