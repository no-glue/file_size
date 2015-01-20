#! /usr/bin/env python
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        quit()
    fileName = sys.argv[1]
    statInfo = os.stat(fileName)
    print statInfo.st_size
