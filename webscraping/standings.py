import pandas as pd
from table2ascii import table2ascii, Alignment

def drivers_standings():
    url = "https://www.formula1.com/en/results.html/2022/drivers.html"
    data = pd.read_html(url)[0]
    data = data[['Pos', 'Driver', 'PTS']]
    # make body = list of lists, where each list element is a row
    output = table2ascii(
        header = ["#", "Driver", "PTS"],
        body = data.values.tolist(),
        first_col_heading = True,
        last_col_heading = True,
        alignments = [Alignment.CENTER] + [Alignment.LEFT] + [Alignment.CENTER]
    );
    return output

def team_standings():
    url = "https://www.formula1.com/en/results.html/2022/team.html"
    data = pd.read_html(url)[0]
    data = data[['Pos', 'Team', 'PTS']]
    data = data.replace(to_replace = "Aston Martin Aramco Mercedes", value = "Aston Martin")
    output = table2ascii(
        header = ["#", "Team", "PTS"],
        body = data.values.tolist(),
        first_col_heading = True,
        last_col_heading = True,
        alignments = [Alignment.LEFT]*3
    );
    return output

def race_wins():
    url = "https://www.formula1.com/en/results.html"
    data = pd.read_html(url)[0]
    data = data[['Grand Prix', 'Winner']]
    output = table2ascii(
        header = ["GP", "Winner"],
        body = data.values.tolist(),
        first_col_heading = True,
        alignments = [Alignment.LEFT]*2
    );
    return output
    



