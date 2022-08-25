from distutils.command.build_scripts import build_scripts


def fizz_buss(input):
    if input %3 == 0 and  input %5 == 0:
        return 'fizz_buss'
    if input %3 == 0:
        return 'fizz'
    if input %5 == 0:
        return 'buss'

    return input


print(fizz_buss(30))