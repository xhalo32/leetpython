# coding: utf-8

from functools import reduce
from math import gcd
from numpy import sign

def factors(n):
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))

def roots(a,b,c):
    s,t = quadratic(a,b,c)
    #print(s,t)
    if not s: return
    gas = gcd(a,s)
    gct = gcd(c,t)
    #print(gas,gct)
    return -s/a, sign(-c*s)*gct/gas

def quadratic(a,b,c):
    f = factors(abs(a*c))
    f = list(f) + [-x for x in f]
    for s in sorted(f):
        t = int(a*c/s)
        if s+t == b:
            return s,t

def main():
    try:
        while 1:
            a,b,c = [int(x) for x in input(" : ").split()]
            print(quadratic(a,b,c))
    except KeyboardInterrupt:
        print()
        quit()

if __name__=='__main__': main()
