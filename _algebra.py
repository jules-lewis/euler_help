'''
-------------------------------------------------------------------------
A collection of (hopefully) useful algebraic functions, to use when
solving Euler Net pronlems.
-------------------------------------------------------------------------
'''
import math
import itertools
compress = itertools.compress

def sum_divisible_by(upper_bound, divisor):
    '''sums all positive integers from 1 to upper_bound,
       divisible by divisor. For example, calling
       sum_divisible_by(10, 3) will return the sum of
       3, 6, and 9.
    '''
    n = upper_bound // divisor
    return int(divisor * sum_numbers(n))


def sum_numbers(upper_bound):
    '''sums all positive integers from 1 to n, using the formula:

         n(n+1)
         ------
           2
    '''
    return int( upper_bound * (upper_bound + 1) / 2)


def get_factors(x):
    '''Finds all the factors of the number passed. It does this
       by checking every integer up to (and including) the square
       root, rounded down. Assumes you'll pass a positive integer,
       and returns a sorted list.
    '''
    factors = []
    for loop in range(1, int(math.sqrt(x))+1):
        if x % loop == 0:
            factors.append(loop)
            newFactor = x // loop
            #the next line checks whether a found factor is the 
            #square root of a square number, so we don't add it
            #to the list twice!
            if newFactor != loop:
                factors.append(newFactor)    
    return sorted(factors)


def get_proper_divisors(x):
    '''Returns a list of all numbers less than n which
       divide evenly into n
    '''
    return get_factors(x)[:-1]


def get_primes(cap):
    '''Returns  a list of primes < cap for cap > 2. 
       Sieve posted by 'Bruno Astrolino' on StackOverflow -
       see https://stackoverflow.com/a/46635266
    '''
    sieve = bytearray([True]) * (cap//2+1)
    for i in range(1,int(cap**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((cap//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,cap,2), sieve[1:])]


def is_prime(x):
    '''checks whether a number is prime by checking that it has
       exactly two factors. Assumes you'll pass a positive integer.
    '''
    if x > 1:
        if len(get_non_trivial_factor_pair(x)) == 0:
            return True
    return False


def get_factor_pairs(x):
    '''Finds all the factors of the number passed and returns them
       as a list of tuples.
    '''
    factorPairs = []
    for loop in range(1, int(math.sqrt(x))+1):
        if x % loop == 0:
            newFactor = x // loop
            factorPairs.append((loop, newFactor))
    return sorted(factorPairs)


def get_non_trivial_factor_pair(x):
    '''Returns the first factor pair of a number n that is not the
       prime factors (1, n). If there isn't a pair (i.e. the number
       is prime, return an empty list
    '''
    factors = []
    for loop in range(2, int(math.sqrt(x))+1):
        if x % loop == 0:
            factors.append(loop)
            factors.append(x // loop)
            break
    return factors


def get_prime_factors(x):
    '''Returns a list containing all the prime factors of the
       supplied number. If the number is prime, it is returned as a
       single item list.
    '''
    factors = get_non_trivial_factor_pair(x)
    if len(factors) != 0:
        return get_prime_factors(factors[0]) + get_prime_factors(factors[1])
    else:
        return [x]


def get_minimum_primes(seedlist):
    '''Returns a sorted list containing the minimum prime numbers
       that can be used to produce each number in the supplied list.
       For instance, if you have a list containing [2, 3, 6], the
       minimum necessary primes is [2, 3], because these can generate
       all the supplied numbers. If more than one instance of a prime
       is needed, e.g. to produce [2, 3, 6, 8] , where 8 needs three 2's,
       the returned list will contain sufficient 2's.
    '''
    minimum_primes = []
    for num in seedlist:
        #ignore 1's
        if num > 1:
            factors = get_prime_factors(num)
            for factor in factors:
                if factor in minimum_primes:
                    while factors.count(factor) > minimum_primes.count(factor):
                        minimum_primes.append(factor)
                else:
                    minimum_primes.append(factor)
    return sorted(minimum_primes)


def get_lowest_common_multiple(seedlist):
    '''Returns the lowest common multiple for any list of positive integers.
    '''
    product = 1
    for prime in get_minimum_primes(seedlist):
        product *= prime
    return product


def get_highest_common_factor(x, y):
    '''Takes two numbers and returns the highest factor of both
    '''
    x_factors = sorted(get_factors(x), reverse=True)
    for factor in x_factors:
        if y % factor == 0:
            return factor
    return 1


def simplify_fraction(fraction):
    '''Takes a tuple of two positive integers (nominator, denominator),
       and returns a tuple with the fraction in its simplest form
    '''
    hcf = get_highest_common_factor(fraction[0], fraction[1])
    return (fraction[0] // hcf, fraction[1] // hcf)


def is_perfect_square(num):
    '''Checks whether a number is square.
    '''
    return int(math.sqrt(num)) == math.sqrt(num)


def is_pentagonal(num):
    '''Checks whether a number is pentagonal, i.e. is in the
       series generated by the formula P{}=n(3n−1)/2. The function
       checks whether applying the inverse function returns an integer.
    '''
    p = (math.sqrt((24 * num) + 1) + 1) / 6
    return p == int(p)


def is_hexagonal(num):
    '''Checks whether a number is hexagonal, i.e. is in the
       series generated by the formula H{}=n(2n−1). The function
       checks whether applying the inverse function returns an integer.
    '''
    p = (math.sqrt((8 * num) + 1) + 1) / 4
    return p == int(p)

def get_number_of_digits(n):
    '''Returns the number of digits in positive integer n.
    '''
    return int(math.log10(n))+1
