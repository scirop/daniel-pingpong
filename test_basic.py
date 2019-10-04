import unittest
import json

import app


class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def testPing(self):
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.data)
        self.assertEqual(json_data['data'], 'pong')

if __name__ == "__main__":
    unittest.main()