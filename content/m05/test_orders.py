import pytest

import orders


ITEMS = [
    {"price": 10, "quantity": 2},
    {"price": 5, "quantity": 4},
]


def test_calculate_total_without_discount():
    assert orders.calculate_total(ITEMS) == 40


def test_calculate_total_with_discount():
    assert orders.calculate_total(ITEMS, discount=10) == 36


def test_apply_discount():
    assert orders.apply_discount(200, 50) == 100


@pytest.mark.parametrize("percent", [-1, 101])
def test_apply_discount_rejects_invalid_percent(percent):
    with pytest.raises(ValueError):
        orders.apply_discount(100, percent)


def test_expensive_items():
    assert orders.expensive_items(ITEMS, 7) == [{"price": 10, "quantity": 2}]


def test_customer_greeting():
    customer = orders.Customer("Ana", "ana@example.com")
    assert customer.name == "Ana"
    assert customer.email == "ana@example.com"
    assert customer.greeting() == "Hello, Ana"
