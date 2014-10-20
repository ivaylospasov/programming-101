import unittest

import entity
import orc


class OrcTest(unittest.TestCase):

    def setUp(self):
        self.torug_orc = orc.Orc("Torug", 100, 1.2)

    def test_hero_init(self):
        self.assertEqual(self.torug_orc.berserk_factor, 1.2)


if __name__ == '__main__':
    unittest.main()
