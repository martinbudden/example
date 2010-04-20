"""
WikiInfo test module.
"""

import unittest
from example import example


class ExampleTestCase(unittest.TestCase):
    """Example test case."""

    def setUp(self):
        """No setUp required."""
        pass

    def tearDown(self):
        """No tearDown required."""
        pass

    def testExample(self):
        """Test example function."""
        print "====testing===="
        result = example.example_function(True)
        expected = True
        self.assertEqual(result, expected)
        self.assertTrue(result)
        #self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
