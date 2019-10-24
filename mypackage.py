def isPrime(n):
    if n<2:
        False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
isPrime(10)