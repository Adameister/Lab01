def calculate_discount(price: float, discount_percent: float) -> float:
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100 percent")
    return price * (1 - discount_percent / 100)


def format_status_message(username: str, status: str) -> str:
    return f"User '{username}' status: [{status.upper()}]"