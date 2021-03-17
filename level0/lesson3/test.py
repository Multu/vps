import unittest

import main


class ConquestCampaignTest(unittest.TestCase):

    def test_one_day(self):
        self.assertEqual(main.ConquestCampaign(1, 1, 1, [1,1]), 1)
        self.assertEqual(main.ConquestCampaign(1, 2, 2, [1,1, 1,2]), 1)
        self.assertEqual(main.ConquestCampaign(1, 3, 3, [1,1, 1,2, 1,3]), 1)
        self.assertEqual(main.ConquestCampaign(2, 2, 4, [1,1, 1,2, 2,1, 2,2]), 1)

    def test_small_area(self):
        self.assertEqual(main.ConquestCampaign(1, 2, 1, [1,1]), 2)
        self.assertEqual(main.ConquestCampaign(1, 2, 1, [1,2]), 2)

        self.assertEqual(main.ConquestCampaign(1, 3, 1, [1,1]), 3)
        self.assertEqual(main.ConquestCampaign(1, 3, 1, [1,2]), 2)
        self.assertEqual(main.ConquestCampaign(1, 3, 1, [1,3]), 3)

        self.assertEqual(main.ConquestCampaign(2, 2, 1, [1,1]), 3)
        self.assertEqual(main.ConquestCampaign(2, 2, 1, [1,2]), 3)
        self.assertEqual(main.ConquestCampaign(2, 2, 2, [1,1, 2,1]), 2)

        self.assertEqual(main.ConquestCampaign(9, 1, 2, [2,1, 9,1]), 4)

        self.assertEqual(main.ConquestCampaign(3, 4, 2, [2,2, 3,4]), 3)

    def test_large_area(self):
        self.assertEqual(main.ConquestCampaign(6, 8, 1, [3,7]), 10)
        self.assertEqual(main.ConquestCampaign(7, 9, 6, [1,8, 2,2, 4,4, 6,6, 7,1, 4,4]), 5)

if __name__ == '__main__':
    unittest.main()
