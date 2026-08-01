import unittest
import json

from app import app


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_tasks(self):
        response = self.app.get('/api/tasks')
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        task_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'priority': 'high',
        }
        response = self.app.post(
            '/api/tasks',
            data=json.dumps(task_data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)

    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
