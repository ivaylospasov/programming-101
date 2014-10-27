import unittest
from song import Song


class SongTest(unittest.TestCase):

    def setUp(self):
        self.song = Song("Twinkle, Twinkle, Little Star", "Jane Taylor",
                         "Rhymes for the Nursery", 4, 153, 128)

    def test_init(self):
        song = Song("Twinkle, Twinkle, Little Star", "Jane Taylor",
                    "Rhymes for the Nursery", 4, 153, 128)
        self.assertEqual(song.title, "Twinkle, Twinkle, Little Star")
        self.assertEqual(song.artist, "Jane Taylor")
        self.assertEqual(song.album, "Rhymes for the Nursery")
        self.assertEqual(song.rating, 0)
        self.assertEqual(song.length, 153)
        self.assertEqual(song.bitrate, 128)

    def test_rate_between_1_and_5(self):
        self.song.rate(3)
        self.assertEqual(self.song.rating, 3)

    def test_rate_value_error(self):
        with self.assertRaises(ValueError):
            self.song.rate(6)
'''
    def test_str(self):
        expected = "ACDC The Jack - 0:04:00"
        self.assertEqual(str(self.song), expected)
'''
if __name__ == '__main__':
    unittest.main()
