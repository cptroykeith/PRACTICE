def fizz_buzz(num):
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizz_buzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else: 
            print(i)
num = int(input('Enter Number: '))
fizz_buzz(num)
