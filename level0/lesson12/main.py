def MassVote(n, votes):
    total_votes = 0
    for i in range(n):
        total_votes += votes[i]

    if total_votes == 0:
        return 'no winner'

    votes_percent = []
    for i in range(n):
        votes_percent.append(round(votes[i] / total_votes * 100, 3))

    winner_index = 0
    winner_percent = 0
    winner_count = 0
    for i in range(n):
        if votes_percent[i] > winner_percent:
            winner_percent = votes_percent[i]
            winner_count = 1
            winner_index = i
        elif votes_percent[i] == winner_percent:
            winner_count += 1


    if winner_percent > 50:
        vote_result = f'majority winner {winner_index + 1}'
    elif winner_count > 1:
        vote_result = 'no winner'
    else:
        vote_result = f'minority winner {winner_index + 1}'

    return vote_result
