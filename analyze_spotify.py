import csv
import ast

lines = []
#with open("top_50_2023.csv", "r") as file:
#    columns = next(file)
#    for line in file:
#        line = line[:-1].split(",")
#        lines.append(line)
#artist_name = 0
#for line in lines:
#    print(line[artist_name])
sum_dance = 0
explicit_songs = 0
with open("top_50_2023.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        lines.append(row)

danceability = header.index("danceability")
explicit = header.index("is_explicit")

for line in lines:
    if line[explicit] == "True":
        explicit_songs += 1

#print(explicit_songs)

for row in lines:
    row[4] = ast.literal_eval(row[4])
#print(lines)

Genres = 4
genres_dict = {}
for row in lines:
    #print(row)
    for genre in row[Genres]:
        if genre in genres_dict:
            genres_dict[genre] += 1
        else:
            genres_dict[genre] = 1
top_three = sorted(genres_dict.items(), key=lambda x: x[1], reverse=True)[:3]
print(top_three)