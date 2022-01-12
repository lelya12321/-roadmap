def is_prime(n):
    'Return True if n is a prime number otherwise return False'


    if n == 1 or n==0:
            return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True