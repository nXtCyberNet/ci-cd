import unittest
from app import app

class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_users(self):
        response = self.app.get('/api/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_user(self):
        response = self.app.get('/api/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "Alice")

        response = self.app.get('/api/users/999')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        new_user = {"name": "Charlie", "email": "charlie@example.com"}
        response = self.app.post('/api/users', json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], "Charlie")

        # Test for missing name or email
        response = self.app.post('/api/users', json={})
        self.assertEqual(response.status_code, 400)

    def test_delete_user(self):
        response = self.app.delete('/api/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "User deleted")

if __name__ == '__main__':
    unittest.main()
