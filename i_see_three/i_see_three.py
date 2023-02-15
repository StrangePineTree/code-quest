import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [int(val) for val in line.split(SEPARATOR)]
    args.sort()
    a = 0
    for _ in range(len(args)):
        if _+4 < len(args):
            if args[_] == args[_+1] and args[_] == args[_+2] and args[_] != args[_+4]:
                print("true")
                a = 1
                break
    if a == 0:
        print("false")