import unittest

import task11_2


class Mailtest(unittest.TestCase):
    def test_change_char(self):
        self.assertNotEqual(task11_2.change_char('somebody_email@gmail.com'), 'somebody_email@gmail.com')  ##NotEqual


if __name__ == "__main__":
    unittest.main
