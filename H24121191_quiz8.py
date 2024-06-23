east = []
west = []
pf = 0
pa = 0
with open("nba_standings.csv", "r") as f:
    line = f.readline()
    line = f.readline().split(",")
    while len(line) > 1:
        if "Eastern" in line:
            if float(line[3]) > 0.5:
                east.append(line[1])
                pf += float(line[5])
                pa += float(line[6])
        if "Western" in line:
            home_win, home_lose = map(int, line[7].split("-"))
            away_win, away_lose = map(int, line[8].split("-"))
            home_rate = home_win / (home_win + home_lose)
            away_rate = away_win / (away_win + away_lose)
            if home_rate < away_rate:
                west.append(line[1])
        line = f.readline().split(",")
pf_ave = pf / len(east)
pa_ave = pa / len(east)
print("question1:", east)
print("question2:", west)
print("question3:", pf_ave - pa_ave)

