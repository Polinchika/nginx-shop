import unittest
from app import app

class TestProductsEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_products(self):
        response = self.client.get("/api/products")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
