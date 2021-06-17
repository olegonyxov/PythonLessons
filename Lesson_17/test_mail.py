import unittest
import task11_2

class Mailtest(unittest.TestCase):
    def test_change_char(self):
        self.assertNotEquals(task11_2.change_char('somebody_email@gmail.com'), 'somebody_email@gmail.com')

if __name__ == "__main__":
    unittest.main
