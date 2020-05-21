import unittest
from flask_boilerplate.app import app


class ExampleTest(unittest.TestCase):
    client = app.test_client()

    def test_basic(self):
        res = self.client.get('/api/hc')

        self.assertEqual(200, res.status_code)
        self.assertDictEqual(res.json, {'message': 'ok'})


if __name__ == "__main__":
    unittest.main()
