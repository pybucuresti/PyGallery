import unittest
import pygallery
import os
import tempfile
import shutil


class TestPyGallery(unittest.TestCase):
    def setUp(self):
        self.temp_folder = tempfile.mkdtemp()
        shutil.copytree(os.path.join(os.path.dirname(__file__), 'pics'),
                        os.path.join(self.temp_folder, 'pics'))
        self.path = os.path.join(self.temp_folder, 'pics')

    def tearDown(self):
        shutil.rmtree(self.temp_folder)

    def test_cmd_arguments(self):
        params = [1,2,3]
        result = pygallery.main(params)
        self.assertEqual(result, params)

    def test_read_folder_contents(self):
        expected = ['pic-true.jpg']
        result = pygallery.read_folder(self.path)
        self.assertEqual(result, expected)

    def test_thumbnails(self):
        result = pygallery.read_folder(self.path)
        pygallery.make_thumbnails(self.path, result)
        expected = ['pic-true.jpg']
        thumb_path = os.path.join(self.path, 'thumbnail')
        thumb_result = pygallery.read_folder(thumb_path)
        self.assertEqual(expected, thumb_result)
        pygallery.clean_thumbnail_dir(self.path)
        self.assertFalse(os.path.isdir(thumb_path))

    def test_indexhtml_exists(self):
        result = pygallery.read_folder(self.path)
        pygallery.make_thumbnails(self.path, result)
        pygallery.generate_indexhtml(self.path, result)
        self.assertTrue(os.path.isfile(os.path.join(self.path, "index.html")))

if __name__ == "__main__":
    unittest.main()
