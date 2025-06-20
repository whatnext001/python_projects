import datetime as dt

competition = "FIFA CLUB WORLD CUP FIXTURES"
print(competition)
time = dt.date.today()
 
teams = ['man utd','man city','chelsea','liverpool','arsenal','totenham','barcelona']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} vs {away_team} on {time}")

