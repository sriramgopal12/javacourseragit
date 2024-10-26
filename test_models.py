import unittest
from factories import create_fake_product

class TestProductModel(unittest.TestCase):

    def test_create_product(self):
        product = create_fake_product()
        self.assertEqual(product.name, "Sample Product")

    def test_update_product(self):
        product = create_fake_product()
        product.name = "Updated Product"
        self.assertEqual(product.name, "Updated Product")

if __name__ == '__main__':
    unittest.main()
