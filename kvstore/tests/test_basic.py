import unittest
from mock import patch

from kvstore.parser import Parser


class TestBasic(unittest.TestCase):
    def setUp(self):
        patch_read_file = patch('kvstore.io._read_file')
        self.mock_read_file = patch_read_file.start()
        self.addCleanup(patch_read_file.stop)
        patch_write_file = patch('kvstore.io._write_file')
        self.mock_write_file = patch_write_file.start()
        self.addCleanup(patch_write_file.stop)

    def _set_input(self, data):
        self.mock_read_file.return_value = data

    def _get_output(self):
        last_call = self.mock_write_file.mock_calls[-1]
        name, args, kwargs = last_call
        return args[1]

    def test_start(self):
        self._set_input("")
        Parser().run(['h', '5'])
        self.assertEqual(
            'h: 5\n',
            self._get_output())

    def test_add(self):
        self._set_input("a: 4")
        Parser().run(['h', '5'])
        self.assertEqual(
            'a: 4\nh: 5\n',
            self._get_output())

    def test_order(self):
        self._set_input("b: 4")
        Parser().run(['a', '5'])
        self.assertEqual(
            'a: 5\nb: 4\n',
            self._get_output())

    def test_replace(self):
        self._set_input("a: 4")
        Parser().run(['a', '5'])
        self.assertEqual(
            'a: 5\n',
            self._get_output())

    def test_format(self):
        self._set_input("a: '5.123'")
        Parser().run(['h', 'hello'])
        print self._get_output()
        self.assertEqual(
            'a: 5.123\nh: hello\n',
            self._get_output())
