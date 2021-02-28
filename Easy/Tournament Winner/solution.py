#https://www.algoexpert.io/questions/Tournament%20Winner

SINGLE_MATCH_WINNER_IDENTIFIER = 1
POINTS = 3

def tournamentWinner(competitions, results):
	score_map = {}
	current_best_team = ''
	score_map[current_best_team] = 0
	for i, match_array in enumerate(competitions):
		result = results[i]
		home_team, away_team = match_array
		winner = home_team if result is SINGLE_MATCH_WINNER_IDENTIFIER else away_team
		update_score(winner, POINTS, score_map)
		if score_map[winner] > score_map[current_best_team]:
			current_best_team = winner
	return current_best_team

def update_score(winner, points, score_map):
	if winner in score_map:
		score_map[winner] += points
	else:
		score_map[winner] = points
