#!/usr/bin/python3
"""
Prime Game module.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Parameters:
        x (int): Number of rounds.
        nums (list): Array containing the upper limit for each round.

    Returns:
        str: Name of the player that won the most rounds ("Maria" or "Ben").
             If the winner cannot be determined, return None.
    """
    def sieve_of_eratosthenes(n):
        """Returns a list of booleans where True indicates a prime number."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime numbers.
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    # Calculate the largest value in nums for the prime sieve
    max_n = max(nums) if nums else 0
    prime_sieve = sieve_of_eratosthenes(max_n)

    # Precompute prime counts for each number up to max_n
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if prime_sieve[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 0:  # Even number of primes -> Ben wins
            ben_wins += 1
        else:  # Odd number of primes -> Maria wins
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
