import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [val for val in line.split(SEPARATOR)]

    if args[0] == args[1]:
        print("true")
    else:
        print("false")