#! /usr/bin/env python
import sys
import os
import argparse

def size(format, file):
    statInfo = os.stat(file)
    if format == "b":
        return round(float(statInfo.st_size), 2)
    elif format == "mb":
        return round(float(statInfo.st_size) / 1024 / 1024, 2)
    elif format == "gb":
        return round(float(statInfo.st_size) / 1024 / 1024 / 1024, 2)
    return 0

if __name__ == "__main__":
    argv = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('-format')
    parser.add_argument('-file')
    args = parser.parse_args(argv)
    print size(args.format, args.file)
