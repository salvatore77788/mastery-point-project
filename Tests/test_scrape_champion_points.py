import unittest
import scrape_champion_points

class TestScrapeChampionPoints(unittest.TestCase):

    def setUp(self):
        self.mastered_row_sample = r"Rek'Sai 7 332,211 5/13/22, 10:58 PM Mastered N/A"
        self.unmastered_row_sample = r""
        self.champion_name_with_space = r""
        self.less_than_4_digit_points = r""

    def tearDown(self):
        pass

    def test_get_champion_points(self):

        self.assertEqual(
            ("Rek'Sai", 332211),
            scrape_champion_points.get_champion_points(self.mastered_row_sample)
        )



if __name__ == '__main__':
    unittest.main()