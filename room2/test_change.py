import pytest

import change

@pytest.mark.parametrize("amount, expected",
  (
    (7, [5, 2]),
    (8, [5, 2, 1]),
    (100, [100]),
    (444, [200, 200, 20, 20, 2, 2]),
    (sum(change.valid_denominations), change.valid_denominations[::-1])
  ),
)
def test_make_change(amount, expected):
  assert change.make_change(amount) == expected
  assert change.make_change2(amount) == expected


@pytest.mark.parametrize("amount, register, expected",
(
  (10, [10], [10]),
  (10, [5, 5, 1], [5, 5]),
  (10, [5, 2, 2, 1], [5, 2, 2, 1]),
  (50, [100, 10], [100]),
  (50, [200, 100, 100, 10], [100]),
  #(150, [200, 100, 100, 10], [100, 100]),
)
)
def test_make_change_from_register(amount, register, expected):
  assert change.make_change_from_register(amount, register) == expected
