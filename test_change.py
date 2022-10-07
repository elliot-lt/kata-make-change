import change
import pytest

@pytest.mark.parametrize("amount,expected_result", 
[
(7, [5, 2]),
(70, [50, 20]),
(100, [100]),
(50000, [50000]),
(49999, [20000, 20000, 5000, 2000, 2000, 500, 200, 200, 50, 20, 20, 5, 2, 2])
])
def test_make_change(amount, expected_result):
  assert change.make_change(amount) == expected_result
 
def test_zero_amound():
  # maybe raise an exception when the amount is 0
  assert change.make_change(0) == []


@pytest.mark.parametrize("amount,available_coins,expected_result", 
[
(5000, {2000: 1, 1000: 2, 500: 1, 100: 100}, [2000, 1000, 1000, 500, 100, 100, 100, 100, 100]),
#(70, [50, 20]),
#(100, [100]),
#(50000, [50000]),
#(49999, [20000, 20000, 5000, 2000, 2000, 500, 200, 200, 50, 20, 20, 5, 2, 2])
])
def test_make_change_with_available_coins(amount, available_coins, expected_result):
  assert change.make_change_limited_coins(amount, available_coins) == expected_result