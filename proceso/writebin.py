from struct import pack
from sys import argv


def writebin(output, rows, cols):
    with open(output, "wb") as fd:
        for r in xrange(0, rows):
            for c in xrange(0, cols):
                fd.write(pack('f', -9999000.000))

if __name__ == '__main__':
    if len(argv) > 3:
        writebin(argv[1], int(argv[2]), int(argv[3]))
