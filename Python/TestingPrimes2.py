""" Find the largest prime of a number """


def get_factors(number):
    factors = []
    for integer in xrange(1, number + 1):
        if number%integer == 0:
            factors.append(integer)
    return factors

def test_prime(number):
    prime = True
    if number == 1 or number == 2:
        return prime
    else:
        for i in xrange(2, number):
            if number%i == 0:
                prime = False
    return prime


def test_for_primes(lst):
    primes = []
    for i in lst:
        if test_prime(i):
            primes.append(i)
    return primes

program starts here
def find_largest_prime_factor(i):
    factors = get_factors(i)
    print factors
    prime_factors = test_for_primes(factors)
    return prime_factors


print find_largest_prime_factor(x)