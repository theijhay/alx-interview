#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    maria_win, ben_win = 0, 0
    n = max(nums)
    primelist = [True for _ in range(1, n + 1, 1)]
    primelist[0] = False
    for i, is_prime in enumerate(primelist, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primelist[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primelist[0: n])))
        ben_win += primes_count % 2 == 0
        maria_win += primes_count % 2 == 1
    if maria_win == ben_win:
        return None
    return 'Maria' if maria_win > ben_win else 'Ben'