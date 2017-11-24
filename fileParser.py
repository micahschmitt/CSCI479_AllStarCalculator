import csv
import fileinput


INPUT_FILE = "data.csv"
NUM_MIN_GAMES = 5

with open(INPUT_FILE, 'r') as i, open('data_parsed.csv', 'w', newline='') as o:
    writer = csv.writer(o)
    for row in csv.reader(i):
        if int(row[8]) >= NUM_MIN_GAMES:
            writer.writerow(row)

