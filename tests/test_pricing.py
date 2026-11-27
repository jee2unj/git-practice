# test_pricing.py

import pytest
from orderlab.pricing import final_total, subtotal


# Level 1
def test_subtotal_normal():  # 정상
    assert subtotal(20_000, 3) == 60_000


def test_subtotal_zero():  # 경계값
    assert subtotal(0, 3) == 0


def test_subtotal_negative():  # 예외
    with pytest.raises(ValueError):
        subtotal(-100, 2)


# Level 2
def test_discount_below_zero():
    with pytest.raises(ValueError):  # 예외가 발생해야 pass
        final_total(10_000, 2, -1)


def test_discount_over_100():
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10_00, 2, 101)
