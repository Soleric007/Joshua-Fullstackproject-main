import uuid

def generate_uuid():
    """Generate a new UUID"""
    return str(uuid.uuid4())

def calculate_total(items: list):
    """Calculate total price of items (each item must have 'price' and 'quantity')"""
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total