# 1792816 Anthony Flores 10.15

class Team:
    def __init__(self, name='none', wins=0, losses=0):
        self.team_name = name
        self.team_wins = wins
        self.team_losses = losses

    def get_win_percentage(self):
        percentage = self.team_wins / (self.team_wins + self.team_loses)
        return float(percentage)


if __name__ == '__main__':

    student_team = Team()
    team_name = input()
    team_wins = int(input())
    team_loses = int(input())

    student_team.team_name = team_name
    student_team.team_wins = team_wins
    student_team.team_loses = team_loses

    if student_team.get_win_percentage() >= 0.5:
        print(f'Congratulations, Team {student_team.team_name} has a winning average!')
    else:
        print(f'Team {student_team.team_name} has a losing average.')
