import unittest
import task1

class Ziptest(unittest.TestCase):
    def test_end_dict(self):
        self.assertEqual(task1.end_dict(3,4),(3,4))

if __name__ == "__main__":
    unittest.main