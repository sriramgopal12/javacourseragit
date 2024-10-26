import unittest
from app import app

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_list_all_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
