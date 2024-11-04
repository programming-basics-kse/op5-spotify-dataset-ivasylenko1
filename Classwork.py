import csv
lines = []

def task2():
    liveness_sum = 0
    counter = 0
    for line in lines:
        if float(line[energy]) > 0.5:
            counter += 1
            liveness_sum += float(line[liveness])
    print(liveness_sum / counter)


def task3():
    artist = header.index('artist_name')
    artist_track = {}
    for line in lines:
        print(line[artist])
        if line[artist] in artist_track:
            artist_track[line[artist]] += 1
        else:
            artist_track[line[artist]] = 1

    top_three = sorted(artist_track.items(), key=lambda x: x[1], reverse=True)[:3]
    print(top_three)


def task5():
    year = header.index('album_release_date')

    year_count = {}
    for line in lines:
        year_split = line[year].split('-')
        if year_split[0] in year_count:
            year_count[year_split[0]] += 1
        else:
            year_count[year_split[0]] = 1
    top = sorted(year_count.items(), key=lambda x: x[1], reverse=True)[0]
    print(top)

with open("top_50_2023.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        lines.append(row)
liveness = header.index("liveness")
energy = header.index("energy")

task2()
task3()
task5()