#!/usr/bin/python3
"""
Prime Game Module
"""


def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, max_n + 1) if is_prime[p]]
    return primes, is_prime


def play_game(n, primes, is_prime):
    game_state = [True] * (n + 1)
    current_player = 0  # 0 for Maria, 1 for Ben

    for prime in primes:
        if prime > n:
            break
        if game_state[prime]:
            for multiple in range(prime, n + 1, prime):
                game_state[multiple] = False
            current_player = 1 - current_player

    return 1 - current_player  # Return the loser (0 for Maria, 1 for Ben)


def isWinner(x, nums):
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes, is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes, is_prime)
        if winner == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
