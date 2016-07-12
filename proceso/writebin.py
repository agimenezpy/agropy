from struct import pack
from sys import argv
from os import path as pth
import re


def writebin(template, year, rows, cols):
    output = re.sub("_(:?[0-9]{4})", "_" + year, pth.basename(template))
    with open(output, "wb") as fd:
        for r in xrange(0, rows):
            for c in xrange(0, cols):
                fd.write(pack('f', -9999000.000))

if __name__ == '__main__':
    if len(argv) > 3:
        writebin(argv[1], argv[2], int(argv[3]), int(argv[4]))
