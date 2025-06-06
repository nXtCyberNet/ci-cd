import unittest
import requests

BASE_URL = "http://localhost:5000"  # Replace with container IP if running externally

class TestFlaskAPI(unittest.TestCase):
    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/api/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_user(self):
        response = requests.get(f"{BASE_URL}/api/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Alice")

        response = requests.get(f"{BASE_URL}/api/users/999")
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        new_user = {"name": "Charlie", "email": "charlie@example.com"}
        response = requests.post(f"{BASE_URL}/api/users", json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "Charlie")

        # Test for missing name or email
        response = requests.post(f"{BASE_URL}/api/users", json={})
        self.assertEqual(response.status_code, 400)

    def test_delete_user(self):
        response = requests.delete(f"{BASE_URL}/api/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "User deleted")

if __name__ == '__main__':
    unittest.main()
