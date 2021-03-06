import math

x = int(input())


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


for n in range(100005):
    if n >= x and is_prime(n):
        print(n)
        break
