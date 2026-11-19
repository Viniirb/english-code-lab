# Calculate the total of an order
def calculate_total(items, discount=0):
    """Add the price of the items and apply the discount."""
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return apply_discount(total, discount)


def apply_discount(value, percent):
    # percent goes from 0 to 100
    if percent < 0 or percent > 100:
        raise ValueError("invalid percent")
    return value - value * percent / 100


def expensive_items(items, limit):
    # return the items with a price above the limit
    return [item for item in items if item["price"] > limit]


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greeting(self):
        return "Hello, " + self.name
