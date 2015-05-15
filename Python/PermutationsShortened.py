from itertools import permutations
from random import randomint
a,b,c,d,n = 1,4,3,2,65
print(sorted(set([''.join(p) for p in permutations(a * "a" + b * "b" + c * "c" + d * "d")]))[n-1])