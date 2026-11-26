def calculate_total(subtotal: float, tax_rate: float = 0.10) -> float:
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")
    return round(subtotal * (1 + tax_rate), 2)
