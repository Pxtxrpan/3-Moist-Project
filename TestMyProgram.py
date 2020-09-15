import unittest

import main as prog

class TestValidator(unittest.TestCase):
    def testtotal(self):
        self.assertEqual(prog.total, 55045469)

    def testmean(self):
        self.assertEqual(prog.mean, 18348489.67)

if __name__ == 'Project':
    unittest.main()