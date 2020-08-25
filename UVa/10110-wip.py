import sys
import math


def main():
    ns = []
    for line in sys.stdin:
        n = int(line)
        if n == 0: break
        else: ns.append(n)
    
    maxlen = max(ns)

    sieve = [True] * (maxlen+1)
    i = 2
    while i < maxlen:
        i += 2
        sieve[i] = False
    p = 3
    while p*p <= maxlen:
        sieve[p] = True
        # starting from p*p, mark multiples of p as 0
        i = p*p
        while i < maxlen:
            sieve[i] = False
            i += p
        # go to next p
        while True:
            p += 2
            if sieve[p]: break

    for n in ns:
        if sieve[n]: print("no")
        else:
            p = 2
            factors = {}
            while n != 1:
                if p not in factors: factors[p] = 0
                while n % p == 0:
                    factors[p] += 1
                    n //= p
                # print(f"finished dividing by {p}, left with {n}, factors are {factors}")
                if (factors[p] + 1) % 2 == 0:
                    print("no")
                    break
                if n != 1:
                    if sieve[n]:
                        print("no")
                        break
                    else:
                        while True:
                            if p == 2: p = 3
                            else:
                                p += 2
                                if sieve[p]: break
                else:
                    # print("computing totient")
                    totient = 1
                    for factor_cnt in factors.values():
                        totient *= factor_cnt + 1
                    # print(totient)
                    if totient % 2 == 0: print("no")
                    else: print("yes")


if __name__ == "__main__":
    main()
