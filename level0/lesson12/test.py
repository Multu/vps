import unittest
import random

import main


class BigMinusTest(unittest.TestCase):

    def test_reflection(self):
        data = [
            [[60, 10, 10, 15, 5], 'majority winner 1'],
            [[10, 15, 10], 'minority winner 2'],
            [[111, 111, 110, 110], 'no winner'],
            [[0, 1, 2, 3, 4, 5], 'minority winner 6'],
            [[0], 'no winner'],
            [[0, 0, 0], 'no winner'],
            [[0, 1, 0], 'majority winner 2'],
        ]

        for i in range(len(data)):
            dataset = data[i]
            self.assertEqual(main.MassVote(len(dataset[0]), dataset[0]), dataset[1])

    def test_random_majority(self):
        majority_vote = 51
        total_vote = 100

        for i in range(1000):
            votes = [majority_vote]
            while sum(votes) < total_vote:
                new_vote = random.randint(0, total_vote - majority_vote)
                if sum(votes) + new_vote > total_vote:
                    pass
                else:
                    votes.append(new_vote)

            random.shuffle(votes)
            majority_index = votes.index(majority_vote) + 1
            self.assertEqual(main.MassVote(len(votes), votes), f'majority winner {majority_index}')

    def test_random_minority(self):
        minority_vote = 50
        total_vote = 100

        for i in range(1000):
            votes = [minority_vote]
            while sum(votes) < total_vote:
                new_vote = random.randint(0, 49)
                if sum(votes) + new_vote > total_vote:
                    pass
                else:
                    votes.append(new_vote)

            random.shuffle(votes)
            minority_index = votes.index(minority_vote) + 1
            self.assertEqual(main.MassVote(len(votes), votes), f'minority winner {minority_index}')

    def test_random_no_winner(self):
        no_winner_vote = 30
        total_vote = 100

        for i in range(1000):
            votes = [no_winner_vote, no_winner_vote]
            while sum(votes) < total_vote:
                new_vote = random.randint(0, 20)
                if sum(votes) + new_vote > total_vote:
                    pass
                else:
                    votes.append(new_vote)

            random.shuffle(votes)
            self.assertEqual(main.MassVote(len(votes), votes), f'no winner')

if __name__ == '__main__':
    unittest.main()
