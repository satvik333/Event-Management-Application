class createdFixtures:
    def print_created_fixtures(fixturesJson):
        try:
            print("Created Fixtures are", fixturesJson)
        except Exception as e:
            print('Error while printing created fixtures:', e)