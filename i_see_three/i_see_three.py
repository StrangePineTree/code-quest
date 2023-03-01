import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [int(val) for val in line.split(SEPARATOR)]
    args.sort()
    a = True
    for i in range(len(args)):
        if i+4 < len(args):
            if args[i] == args[i+1] and args[i] == args[i+2] and args[i] != args[i+4]:
                print("TRUE")
                a = False
                break
    if a:
        print("FALSE")