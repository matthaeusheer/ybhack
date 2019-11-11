import unittest

from ybhack.dummylib import libfile


class TestDummyLib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(libfile.add(1, 2), 3, "1 + 2 should be 3!")

    def test_add_wrong(self):
        self.assertNotEqual(libfile.add_wrong(1, 2), 3, "1 + 2 should not be 3 for the bugged add function!")
