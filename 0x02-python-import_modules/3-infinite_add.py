#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    value = 0
    for i in range(len(sys.argv) - 1):
        value = value + int(sys.argv[i + 1])
    print("{}".format(value))
