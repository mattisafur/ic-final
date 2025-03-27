import unittest


import src.app as app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app.app_context()
        self.ctx.push()
        self.client = app.app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_is_online(self):
        self.assertFalse(app.is_online("https://google.com/doesnotexist"))
        self.assertTrue(app.is_online("https://example.com/"))

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.json, {"message": "Usage: /status/<url>"})


if __name__ == "__main__":
    unittest.main()
