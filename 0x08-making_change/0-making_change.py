#!/usr/bin/python3
"""
Define make change function
"""


def makeChange(coins, total):
    """ Base cases """
    if total <= 0:
        return 0

    """ Initialize an array to store the minimum
    number of coins needed for each amount """
    dp = [float('inf')] * (total + 1)

    """ Base case: 0 coins needed for amount 0 """
    dp[0] = 0

    """ Iterate through all amounts from 1 to total """
    for amount in range(1, total + 1):
        """ Iterate through all coin denominations """
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    """ Check if a valid solution exists """
    if dp[total] == float('inf'):
        return -1

    """ The result is stored at the index representing the total amount """
    return dp[total]
