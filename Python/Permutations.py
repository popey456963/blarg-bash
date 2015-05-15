from itertools import permutations
print(sorted(set([''.join(p) for p in permutations(0 * "a" + 2 * "b" + 1 * "c" + 3 * "d")])))