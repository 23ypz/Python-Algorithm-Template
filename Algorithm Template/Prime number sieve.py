"""
质数筛分为埃氏筛和欧拉筛
时间复杂度分别为 O(nlog log n)和 O(n)
其实log log n非常小，几乎可以当作一个常数，所以二者几乎没区别
选一个记就好了
"""

MX = 10 ** 6 + 1


def Ehrlich_sieve():
    primes = []
    is_prime = [True] * MX
    is_prime[0] = is_prime[1] = False
    for i in range(2, MX):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, MX, i):
                is_prime[j] = False
    return is_prime, primes


def Euler_sieve():
    primes = []
    is_prime = [True] * MX
    is_prime[0] = is_prime[1] = False
    for i in range(2, MX):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p >= MX: break
            is_prime[i * p] = False
            if i % p == 0: break
    return is_prime, primes
