def printNto1(n):
    if n == 0:
        return

    print(n)
    printNto1(n - 1)

    # this is tail recursive solution, because recursion is the last thing which happening in this code, nothing left to execute after recursive call.

    # Output -

    # 5
    # 4
    # 3
    # 2
    # 1


def print1toN(n):
    if n == 0:
        return

    print1toN(n - 1)
    print(n)

    # this is non-tail recursive soution, because after recursion, there still code left to excecute.

    # Output -

    # 1
    # 2
    # 3
    # 4
    # 5


def printEveryNumberTwiceExeptLargest(n):
    if n == 0:
        return

    printEveryNumberTwiceExeptLargest(n - 1)
    print(n)
    printEveryNumberTwiceExeptLargest(n - 1)

    # this will print every twice except the largest one, largest come into the middle.
    # e.g. for n = 3, output will be 1 2 1 3 1 2 1

    # Output -

    # 1
    # 2
    # 1
    # 3
    # 1
    # 2
    # 1


def printNto1and1toN(n):
    if n == 0:
        return

    print(n)
    printNto1and1toN(n - 1)
    print(n)

    # Output -

    # 5
    # 4
    # 3
    # 2
    # 1
    # 1
    # 2
    # 3
    # 4
    # 5


def print1toNandNto1(n, x):
    if x > n:
        return

    print(x)
    print1toNandNto1(n, x + 1)
    print(x)

    # Output -

    # 1
    # 2
    # 3
    # 4
    # 5
    # 5
    # 4
    # 3
    # 2
    # 1


def printDecimalToBinary(n):
    if n == 0:
        return

    printDecimalToBinary(n // 2)
    print(n % 2, end="")

    # in this we are reducing n by dividing with 2 and printing the n by moding with 2 in reverse order i.e. non-tail recursive way, so it will print in reverse manner.

    # Output - 1010


def printStars(n, x):
    if n == 0:
        return

    print("*" * x)
    printStars(n - 1, x)

    # Output -

    # *****
    # *****
    # *****
    # *****
    # *****


def print1toNStars(n, x):
    if n == 0:
        return

    print("*" * x)
    print1toNStars(n - 1, x + 1)

    # Output -

    # *
    # **
    # ***
    # ****
    # *****


def printNto1Stars(n):
    if n == 0:
        return

    print("*" * n)
    printNto1Stars(n - 1)

    # Output -

    # *****
    # ****
    # ***
    # **
    # *


def printNto1LadderRow(n):
    if n == 0:
        return

    print(str(n) * n)
    printNto1LadderRow(n - 1)

    # Output -
    # 55555
    # 4444
    # 333
    # 22
    # 1


def print1toNLadderRow(n):
    if n == 0:
        return

    print1toNLadderRow(n - 1)
    print(str(n) * n)

    # Output -
    # 1
    # 22
    # 333
    # 4444
    # 55555


def print_row(k):
    if k == 0:
        return
    print_row(k - 1)
    print(k, end="")


def printNto1LadderCol(n):
    if n == 0:
        return
    printNto1LadderCol(n - 1)
    print_row(n)
    print()


n = int(input())

# printNto1(n)

# print1toN(n)

# printEveryNumberTwiceExeptLargest(n)

# printNto1and1toN(n)

# print1toNandNto1(n, 1)

# printDecimalToBinary(n)

# printStars(n, n)

# print1toNStars(n, 1)

# printNto1Stars(n)

# printNto1LadderRow(n)

# print1toNLadderRow(n)

printNto1LadderCol(n)
