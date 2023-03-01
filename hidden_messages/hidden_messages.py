import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

letters = sys.stdin.readline().rstrip()

for caseNum in range(cases - 1):
    line = sys.stdin.readline().rstrip()
    args = [word for word in line.split(SEPARATOR)]
    for i, word in enumerate(args):
        letterzz = [i for i in word.split("-")]
        for num in letterzz:
            print(letters[int(num)-1], end="")
        if i + 1 != len(args):
            print(" ", end="")
    print()
    