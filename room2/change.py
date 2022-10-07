from typing import List
# Representing the number of cents in valid euro coins/notes
valid_denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]


def find_smallest(amount: int) -> int:
  for value in valid_denominations[::-1]:
    if value <= amount:
      return value
  raise ValueError

def make_change(amount: int) -> List[int]:
  denominations = []
  running_count = amount
  while running_count > 0:
    smallest = find_smallest(running_count)
    denominations.append(smallest)
    running_count -= smallest
  return denominations

def make_change2(amount: int) -> List[int]:
  denominations = []
  for value in reversed(valid_denominations):
    while value <= amount:
      amount -= value
      denominations.append(value)
    # if not amount: break

  return denominations
  
def make_change_from_register(amount: int, register: List[int]) -> List[int]:
  denominations = []
  for value in sorted(register, reverse=True):
    if value <= amount:
      amount -= value
      denominations.append(value)
    # if not amount: break

  if sum(denominations) < amount:
    return [min(c for c in register if c >= amount)]

  return denominations