def sumdivisors(n):
    def factors(n):    
        return reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    def sumfactors(n):
        temp = 0
        array = factors(n)
        for i in array:
            temp = temp + i
        return temp
    x = sumfactors(n)
    y = sumfactors(x)
    if x == y:
        return n
    else:
        return 0
total = 0
for i in range(900):
    temp2 = sumdivisors(i+1)
    total = total + temp2
print(total)