import unittest
import pygallery
import os


class TestPyGallery(unittest.TestCase):

    def test_cmd_arguments(self):
        params = [1,2,3]
        result = pygallery.main(params)
        self.assertEqual(result, params)

    def test_read_folder_contents(self):
        path = './pics/'
        expected = ['pic-true.jpg']
        result = pygallery.read_folder(path)
        self.assertEqual(result, expected)

    def test_thumbnails(self):
        path = './pics/'
        result = pygallery.read_folder(path)
        pygallery.make_thumbnails(path, result)
        expected = ['pic-true.jpg']
        thumb_path = os.path.join(path, 'thumbnail')
        thumb_result = pygallery.read_folder(thumb_path)
        self.assertEqual(expected, thumb_result)
        pygallery.clean_thumbnail_dir(path)
        self.assertFalse(os.path.isdir(thumb_path))

if __name__ == "__main__":
    unittest.main()
