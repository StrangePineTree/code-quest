import sys

SEPARATOR = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [int(val) for val in line.split(SEPARATOR)]
    args.sort()
    for _ in range(len(args)):
        print(args[_], end = "" if _ == len(args)-1 else ",")
    print("")