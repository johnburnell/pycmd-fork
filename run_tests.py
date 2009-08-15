import unittest
from tests import common_tests

def suite():
    suite = unittest.TestSuite()
    suite.addTest(common_tests.suite())
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')