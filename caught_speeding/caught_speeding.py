import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())
bday = False
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = [val for val in line.split(SEPARATOR)]

    bday = False
    if args[1] == 'true':
        bday = True

    if int(args[0]) <= (65 if bday == True else 60):
        print("no ticket")
    elif int(args[0]) <= (85 if bday == True else 80):
        print("small ticket")
    elif int(args[0]) > (85 if bday == True else 80):
        print("big ticket")
