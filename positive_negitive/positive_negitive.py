import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [int(val) for val in line.split(SEPARATOR)]

    for num in args:
        if num > 0:
            print("POSITIVE")
        else:
            print("NEGATIVE")
    