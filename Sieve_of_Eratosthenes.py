def find_primes(num: int) -> list:
    """
    returns all the prime numbers in a list that are less than the
    supplied number (num)
    """
    non_primes = []
    primes = []

    for i in range(2, num+1):
        if i not in non_primes:
            for n in range(2, round(num/i)+1):
                non_primes.append(i*n)
            primes.append(i)

    return primes


print(find_primes(10000))
