import os

DATAFILE = "music.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        count = 0
        for line in f:
            if count == 10:
                break

            fields = line.split(",")
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            count += 1
    return data
