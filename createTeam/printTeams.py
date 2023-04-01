class createdTeams:
    def print_created_teams(teamsJson):
        try:
            print("Created Teams are", teamsJson)
        except Exception as e:
            print('Error while printing created teams:', e)