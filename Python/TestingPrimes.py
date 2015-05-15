def primetest(x):  
    if x < 2:  
        return False  
    if x == 2:  
        return True  
    if x % 2 == 0:  
        return False  
    for i in range(3,int((x**0.5)+1)):  
        if x % i == 0:  
            return False  
    return True

def nthprime(n):  
    primes = []  
    x = 2  
    while len(primes) < n:  
        if primetest(x) == True:  
            primes.append(x)  
            x = x + 1  
    return primes[-1]

print(nthprime(10))
