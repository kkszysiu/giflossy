import shutil
import os
import tempfile
import unittest

import pygiflossy


class TestGifLossy(unittest.TestCase):

    def setUp(self):
        super(TestGifLossy, self).setUp()
        self.gifs_path = os.path.join(os.path.dirname(__file__), 'gifs')
        self.tests_output_path = tempfile.mkdtemp(prefix='tmp-pygiflossy-tests-')

    def test_gif_optimization_1(self):
        filename = 'orig1.gif'
        gif_filepath = os.path.join(self.gifs_path, filename)
        output_gif_filepath = os.path.join(self.tests_output_path, filename)

        pygiflossy.convert(gif_filepath, output_gif_filepath)

        self.assertTrue(os.path.isfile(output_gif_filepath))

        input_size = os.path.getsize(gif_filepath)
        output_size = os.path.getsize(output_gif_filepath)

        self.assertTrue(input_size > output_size)

    def test_gif_optimization_2(self):
        filename = 'orig2.gif'
        gif_filepath = os.path.join(self.gifs_path, filename)
        output_gif_filepath = os.path.join(self.tests_output_path, filename)

        pygiflossy.convert(gif_filepath, output_gif_filepath)

        self.assertTrue(os.path.isfile(output_gif_filepath))

        input_size = os.path.getsize(gif_filepath)
        output_size = os.path.getsize(output_gif_filepath)

        self.assertTrue(input_size > output_size)

    def test_gif_optimization_3(self):
        filename = 'orig3.gif'
        gif_filepath = os.path.join(self.gifs_path, filename)
        output_gif_filepath = os.path.join(self.tests_output_path, filename)

        pygiflossy.convert(gif_filepath, output_gif_filepath)

        self.assertTrue(os.path.isfile(output_gif_filepath))

        input_size = os.path.getsize(gif_filepath)
        output_size = os.path.getsize(output_gif_filepath)

        self.assertTrue(input_size > output_size)

    def test_gif_optimization_big(self):
        filename = 'orig4.gif'
        gif_filepath = os.path.join(self.gifs_path, filename)
        output_gif_filepath = os.path.join(self.tests_output_path, filename)

        pygiflossy.convert(gif_filepath, output_gif_filepath)

        self.assertTrue(os.path.isfile(output_gif_filepath))

        input_size = os.path.getsize(gif_filepath)
        output_size = os.path.getsize(output_gif_filepath)

        self.assertTrue(input_size > output_size)

    def test_gif_optimization_small(self):
        filename = 'orig5.gif'
        gif_filepath = os.path.join(self.gifs_path, filename)
        output_gif_filepath = os.path.join(self.tests_output_path, filename)

        pygiflossy.convert(gif_filepath, output_gif_filepath)

        self.assertTrue(os.path.isfile(output_gif_filepath))

        input_size = os.path.getsize(gif_filepath)
        output_size = os.path.getsize(output_gif_filepath)

        self.assertTrue(input_size > output_size)

    def test_gif_overwrite(self):
        filename = 'orig6.gif'
        gif_filepath = os.path.join(self.gifs_path, filename)
        gif_copied_path = tempfile.mkdtemp(prefix='tmp-pygiflossy-tests-')
        shutil.copy(gif_filepath, gif_copied_path)
        gif_copied_filepath = output_gif_filepath = os.path.join(gif_copied_path, filename)

        input_size = os.path.getsize(gif_filepath)

        pygiflossy.convert(gif_copied_filepath, output_gif_filepath)

        self.assertTrue(os.path.isfile(output_gif_filepath))

        output_size = os.path.getsize(output_gif_filepath)

        self.assertTrue(input_size > output_size)

    def test_gif_compression_80(self):
        filename = 'orig5.gif'
        gif_filepath = os.path.join(self.gifs_path, filename)
        output_gif_filepath = os.path.join(self.tests_output_path, filename)

        input_size = os.path.getsize(gif_filepath)

        pygiflossy.convert(gif_filepath, output_gif_filepath)

        self.assertTrue(os.path.isfile(output_gif_filepath))

        output_size_compression_default = os.path.getsize(output_gif_filepath)

        self.assertTrue(input_size > output_size_compression_default)

        pygiflossy.convert(gif_filepath, output_gif_filepath, compression_level=80)

        self.assertTrue(os.path.isfile(output_gif_filepath))

        output_size_compression_80 = os.path.getsize(output_gif_filepath)

        self.assertTrue(output_size_compression_default > output_size_compression_80)
