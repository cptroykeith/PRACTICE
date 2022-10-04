''''
def sum(num1, *args):
    total = num1
    for num in args:
        total = total + num
    return total

sum(5,7)
'''''
def my_sum(*args):
    return sum(args)

