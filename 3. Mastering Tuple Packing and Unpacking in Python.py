orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),]

def display_orders(orders):
    for i, order in enumerate(orders, 1):
        name, product, quantity = order
        print(f"Order {i}:  Customer name: {name}; Product: {product}; Product Quantity: {quantity}")

display_orders(orders)