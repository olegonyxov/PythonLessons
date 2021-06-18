import unittest

import task7_2


class Mailtest(unittest.TestCase):
    def test_if_c(self):
        self.assertEqual(task7_2.if_c(10,"c"), "Кельвин:" + str + "Цельсий:" + str + "Фарингейт:" + str)

if __name__ == "__main__":
    unittest.main