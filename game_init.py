from data.teams import ALL_D1_TEAMS
from main import Team, Season

def initialize_game():
    teams = [Team(**team_data) for team_data in ALL_D1_TEAMS]
    current_year = datetime.now().year
    season = Season(year=current_year, teams=teams)
    season.generate_schedule()
    return season