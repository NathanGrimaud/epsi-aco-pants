import csv
import sys
from model.pub import Pub
from ants import create_word, solve


def read_data():
    pubs = set()
    with open('./data/open_pubs.lite.csv') as ifile:
        read = csv.reader(ifile, delimiter=",")
        for row in read:
            name = row[1]
            easting = row[4]
            northing = row[5]
            pubs.add(Pub(name, easting, northing))
    return list(pubs)


def start():
    data = read_data()
    world = create_word(data)
    solve(world)


if __name__ == '__main__':
    start()
