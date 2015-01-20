#! /usr/bin/env python
import sys
import os
import argparse

def size(format, file):
    statInfo = os.stat(file)
    if format == "b":
        return statInfo.st_size
    elif format == "mb":
        return statInfo.st_size / 1024 / 1024
    elif format == "gb":
        return statInfo.st_size / 1024 / 1024 / 1024
    return 0

if __name__ == "__main__":
    argv = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('-format')
    parser.add_argument('-file')
    args = parser.parse_args(argv)
    print size(args.format, args.file)
