from main import Team, Player, AdvancedGame

def setup_teams():
    # Create players for each team
    home_players = [Player(name=f"Home Player {i}", position="QB", rating=85 + i) for i in range(11)]
    away_players = [Player(name=f"Away Player {i}", position="QB", rating=80 + i) for i in range(11)]

    # Create teams
    home_team = Team(name="Home Team", conference="Conference A", historical_rating=90)
    away_team = Team(name="Away Team", conference="Conference B", historical_rating=85)

    # Assign players to teams
    home_team.roster = home_players
    away_team.roster = away_players

    return home_team, away_team

def test_game():
    home_team, away_team = setup_teams()
    game = AdvancedGame(home=home_team, away=away_team)

    # Simulate the game
    game.simulate()

    # Display the final score and stats
    game.display_final_score()

if __name__ == "__main__":
    test_game()