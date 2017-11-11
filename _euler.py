'''
-------------------------------------------------------------------------
A collection of functions that have been helpful in solving Euler Net
problems, but probably don't have a wider application.
-------------------------------------------------------------------------
'''


def is_pandigital_9(s):
    '''Checks whether a string contains the digits 1-9 only.
    '''
    if len(s) == 9:
        if ''.join(sorted(s)) == '123456789':
            return True
    return False


def is_pandigital_10(s):
    '''Checks whether a string contains the digits 0-9 only.
    '''
    if len(s) == 10:
        if ''.join(sorted(s)) == '0123456789':
            return True
    return False

def is_palindrome(s):
    '''Return True if the passed string is palindromic
    '''
    if len(s):
        if s == s[::-1]:
            return True
    return False

