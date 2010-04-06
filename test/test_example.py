"""
Example test module.
"""

import unittest

from example import example


class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExample(self):
        """Test example function."""
        result = example.example_function(True)
        expected = True
        self.assertEqual(result, expected)
        self.assertTrue(result)

        self.assertEqual(example.example_function(False), False)






if __name__ == "__main__":
    unittest.main()