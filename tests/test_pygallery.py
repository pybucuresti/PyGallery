import unittest
import pygallery
import os


class TestPyGallery(unittest.TestCase):

    def test_cmd_arguments(self):
        params = [1,2,3]
        result = pygallery.main(params)
        self.assertEqual(result, params)

    def test_read_folder_contents(self):
        params = './pics/'
        expected = ['pic-true.jpg'];
        result = pygallery.read_folder(params)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
