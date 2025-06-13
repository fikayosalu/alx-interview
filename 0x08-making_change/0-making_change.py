#!/usr/bin/python3
"""  0-making_change """


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    # Set up a DP table filled with 'infinity' for min comparison
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # base case

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
