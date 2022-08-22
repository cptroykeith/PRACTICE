#palindrome are words when reversed they mean the some thing e.g 'level,madam,refer etc'

def palindrome (str_obj):
    if str_obj == str_obj[::-1]:
        return 'palindrome'

    else :
        return 'not palidrome'
        