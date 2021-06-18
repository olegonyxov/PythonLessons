import unittest

import task7_2


class temptest(unittest.TestCase):
    def test_if_c(self):
        self.assertEqual(task7_2.if_c(10,"c"), "Кельвин:" + "283.5" + "Цельсий:" + "10" + "Фарингейт:" + "50")

    def test_if_k(self):
        self.assertEqual(task7_2.if_c(10, "k"), "Кельвин:" + "10" + "Цельсий:" + "263.5" + "Фарингейт:" + "442")

    def test_if_f(self):
        self.assertEqual(task7_2.if_f(10, "f"), "Кельвин:" + "261" + "Цельсий:" + "-23" + "Фарингейт:" + 10)


if __name__ == "__main__":
    unittest.main