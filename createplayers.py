import csv
import random

csv_file = "sample.csv"
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

player_names = [row[0] for row in data[1:]]

transposed_data = [["Player", "Angel", "Mortal"]]

random.shuffle(player_names)

for i in range(len(player_names)):
    player = player_names[i]
    angel = player_names[(i + 1) % len(player_names)]
    mortal = player_names[(i - 1) % len(player_names)]
    transposed_data.append([player, angel, mortal])

csv_file_transposed = "player_data.csv"
with open(csv_file_transposed, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(transposed_data)

print(f"CSV file '{csv_file_transposed}' has been created with transposed and mapped data.")
