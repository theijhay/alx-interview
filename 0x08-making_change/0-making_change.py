#!/usr/bin/python3
"""Greedy Algorithm"""


def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    # Initialize the count of coins
    count = 0

    # Iterate through the sorted coins
    for coin in coins:
        # Use as many of the current coin as possible
        if total >= coin:
            num_coins = total // coin
            total -= num_coins * coin
            count += num_coins

        # If total becomes 0, we have the answer
        if total == 0:
            return count

    # If we exit the loop and total is not 0, return -1
    return -1
