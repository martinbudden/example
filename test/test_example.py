"""
Example test module.
"""

import unittest

from example import example


class exampleTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExample(self):
        """Test example function."""
        self.assertEqual(example.example_function(), True)


if __name__ == "__main__":
    unittest.main()