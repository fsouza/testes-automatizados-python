def is_divisible(x, y):
    return x % y == 0


def is_prime(x):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    return count == 2
