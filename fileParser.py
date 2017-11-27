import csv

INPUT_FILE = "data.csv"
NUM_MIN_GAMES = 5

column_a = 0
player = 1
all_nba = 2
all_star = 3
draft_yr = 4
pk = 5
team = 6
college = 7
yrs = 8
games = 9
minutes_played = 10
pts = 11
trb = 12
ast = 13
fg_percentage = 14
tp_percentage = 15
ft_percentage = 16
minutes_per_game = 17
points_per_game = 18
trb_per_game = 19
assits_per_game = 20
win_share = 21
ws_per_game = 22
bpm = 23
vorp = 24
executive = 25
tenure = 26
exec_id = 27
exec_draft_exp = 28
attend_college = 29
first_year = 30
second_year = 31
third_year = 32
fourth_year = 33
fifth_year = 34


def hasPlayedAllStar(row):
    if int(row[all_star]) > 0:
        return 1
    return -1


def parseFile():
    with open(INPUT_FILE, 'r') as i, open('data_parsed.txt', 'w', newline='') as o:
        writer = csv.writer(o, delimiter =' ')
        for row in csv.reader(i):
            if int(row[8]) >= NUM_MIN_GAMES:
                writer.writerow(row)


# Parses file according to the stats we wanted to look at according to Github
# FG% / FT% / Min per game / rebounds per game / assists per game / hasPlayedAllStar (-1 or 1)
def parseFileCleanedStats():
    with open(INPUT_FILE, 'r') as i, open('data_parsed_cleaned_stats.txt', 'w', newline='') as o:
        writer = csv.writer(o, delimiter =' ')
        for row in csv.reader(i):
            if int(row[8]) >= NUM_MIN_GAMES:
                writer.writerow(
                    (row[fg_percentage], row[ft_percentage], row[minutes_per_game], row[trb_per_game],
                     row[assits_per_game], str(hasPlayedAllStar(row))))


def parseFileClassFirst():
    with open(INPUT_FILE, 'r') as i, open('class_first_parsed_cleaned_stats.txt', 'w', newline='') as o:
        writer = csv.writer(o, delimiter =' ')
        for row in csv.reader(i):
            if int(row[8]) >= NUM_MIN_GAMES:
                writer.writerow(
                    (str(hasPlayedAllStar(row)), row[fg_percentage], row[ft_percentage], row[minutes_per_game], row[trb_per_game],
                     row[assits_per_game]))

parseFileClassFirst()