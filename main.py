# Problem 35:
#     Circular Primes
#
# Description:
#     The number, 197, is called a circular prime because
#       all rotations of the digits: 197, 971, and 719, are themselves prime.
#
#     There are thirteen such primes below 100:
#         2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
#     How many circular primes are there below one million?

from math import floor, sqrt


def main(n):
    """
    Returns an ordered list of all 'circular' primes below `n`.
    Note all rotations will be present in the list,
        e.g. 'abc', 'bca', and 'cab' would all be present.

    Args:
        n (int): Natural number

    Returns:
        (List[int]): Ordered list of all circular primes less than `n`

    Raises:
        AssertError: if incorrect args are given
    """
    # Use Sieve of Eratosthenes to get all primes below `n`
    sieve = []
    for x in range(2, n):
        # Use already found primes to check if `x` prime
        x_is_prime = True
        x_mid = floor(sqrt(x))+1  # Only need to check divisibility up to here
        i = 0
        while i < len(sieve) and sieve[i] < x_mid:
            p = sieve[i]
            if x % p == 0:
                x_is_prime = False
                break
            i += 1
        if x_is_prime:
            sieve.append(x)

    # Look for the circular ones
    primes = set(sieve)
    cps = []
    while len(primes) > 0:
        p = primes.pop()
        ps = str(p)
        if '0' not in ps:
            primes.add(p)
            rotations = list(map(lambda k: int(ps[k:]+ps[:k]), range(len(ps))))
            if all(map(lambda q: q in primes, rotations)):
                # Add all possible rotations at same time
                for r in set(rotations):  # Use set to avoid rotated duplicates
                    cps.append(r)

            # Won't need to check the other rotations anymore
            for r in rotations:
                primes.discard(r)
        else:
            # If '0' a digit of `p`, skip `p` since some rotation will start with 0, which doesn't count
            continue
    cps.sort()
    return cps


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    circular_primes = main(num)
    print('Number of circular primes below {}:'.format(num))
    print('  {}'.format(len(circular_primes)))
    print('Circular primes:')
    for circular_prime in circular_primes:
        print('  {}'.format(circular_prime))
