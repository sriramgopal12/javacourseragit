class Product:
    def __init__(self, name, category, price, available):
        self.name = name
        self.category = category
        self.price = price
        self.available = available

def create_fake_product():
    return Product("Sample Product", "Category1", 10, True)
