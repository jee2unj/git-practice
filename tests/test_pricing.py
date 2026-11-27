# test_pricing.py

import pytest
from orderlab.pricing import subtotal


def test_subtotal_normal():         # 정상
    assert subtotal(20_000, 3) == 50_000

def test_subtotal_zero():           # 경계값
    assert subtotal(0, 3) == 0

def test_subtotal_negative():       # 예외
    with pytest.raises(ValueError):
        subtotal(-100, 2)
