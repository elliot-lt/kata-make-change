from typing import List
from collections import namedtuple
import random
# Representing the number of cents in valid euro coins/notes
valid_denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]


# available_coin = namedtuple("available_coin", "valid_denomination, nr")
# cash = [available_coin(coin, i) for i, coin in enumerate(valid_denominations)]


def make_change_limited_coins(amount: int, available_coins: dict) -> List[int]:
  change = []
  for coin in reversed(valid_denominations):
    if amount == 0:
        return change
    nr_coins = max(amount // coin, available_coins.get(coin, 0))
    change.extend([coin] * nr_coins)
    amount -= coin * nr_coins
  return find_bigger_smallest_coin(amount, available_coins)
  
def find_bigger_smallest_coin(amount: int, available_coins: dict):
  for coin_entry, number in available_coins.items():
    if coin_entry > amount and number > 0:
      return coin_entry
    

def make_change(amount: int) -> List[int]:
  change = []
  for coin in reversed(valid_denominations):
    if amount == 0:
        return change
    nr_coins = amount // coin 
    change.extend([coin] * nr_coins)
    amount -= coin * nr_coins

""""
def make_change_previous(amount: int) -> List[int]:
  if amount == 0:
    return []
  if amount in valid_denominations:
    return [amount]

  coins_to_return = []
  while amount > 0:
    for i, coin in enumerate(valid_denominations):
      if coin > amount:
        index = i-1
        coins_to_return.append(valid_denominations[index])
        amount -= valid_denominations[index]
        break

  return coins_to_return
"""