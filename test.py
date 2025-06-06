import unittest
import requests

BASE_URL = "http://localhost:5000"

class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        # Reset the Flask app's state
        requests.post(f"{BASE_URL}/api/reset")

    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/api/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_user(self):
        response = requests.get(f"{BASE_URL}/api/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Alice")

    def test_create_user(self):
        new_user = {"name": "Charlie", "email": "charlie@example.com"}
        response = requests.post(f"{BASE_URL}/api/users", json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "Charlie")

    def test_delete_user(self):
        response = requests.delete(f"{BASE_URL}/api/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "User deleted")

if __name__ == '__main__':
    unittest.main()
