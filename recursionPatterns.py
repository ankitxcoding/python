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

    # This is non-tail recursive soution, because after recursion, there still code left to excecute, but if can be converted into tail recursive by simply introducing second variable.

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

    # This will print every twice except the largest one, largest come into the middle.
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


def print1toNandNto1(n, x=1):
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

    # In this we are reducing n by dividing with 2, in the recusive function, so that function meet the base case at some point and printing the n by moding with 2 in reverse order i.e. non-tail recursive way, so it will print in reverse manner.

    # Output - 1010


def printStars(n, x):
    if n == 0:
        return

    print("*" * x)
    printStars(n - 1, x)

    # For cases like this always prefer tail recursive approach.

    # Output -

    # *****
    # *****
    # *****
    # *****
    # *****


def print1toNStars(n, x=1):
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


def print1ToNLadderCol(n):
    def printRow(k):
        if k == 0:
            return

        printRow(k - 1)
        print(k, end="")

    if n == 0:
        return

    print1ToNLadderCol(n - 1)
    printRow(n)
    print()

    # Output -

    # 1
    # 12
    # 123
    # 1234
    # 12345


def print1ToNLadderColInverse(n):
    def printRow(k):
        if k == 0:
            return

        printRow(k - 1)
        print(k, end="")

    if n == 0:
        return

    printRow(n)
    print()
    print1ToNLadderColInverse(n - 1)

    # Output -

    # 12345
    # 1234
    # 123
    # 12
    # 1


def printNto1LadderCol(n):
    def printRow(k):
        if k == 0:
            return

        print(k, end="")
        printRow(k - 1)

    if n == 0:
        return

    printNto1LadderCol(n - 1)
    printRow(n)
    print()

    # Output -

    # 1
    # 21
    # 321
    # 4321
    # 54321


def printNto1LadderColInverse(n):
    def printRow(k):
        if k == 0:
            return

        print(k, end="")
        printRow(k - 1)

    if n == 0:
        return

    printRow(n)
    print()
    printNto1LadderColInverse(n - 1)

    # Output -

    # 54321
    # 4321
    # 321
    # 21
    # 1


def triangleStars(n, s=1):
    if s > n:
        return

    print(" " * (n - s) + "*" * (2 * s - 1))
    triangleStars(n, s + 1)

    # Output -

    #     *
    #    ***
    #   *****
    #  *******
    # *********


def triangleStarsInverse(n, s=1):
    if s > n:
        return

    triangleStarsInverse(n, s + 1)
    print(" " * (n - s) + "*" * (2 * s - 1))

    # Output -

    # *********
    #  *******
    #   *****
    #    ***
    #     *


def triangleStarsUpSideDown(n, s=1):
    if s > n:
        return

    print(" " * (n - s) + "*" * (2 * s - 1))
    triangleStarsUpSideDown(n, s + 1)
    print(" " * (n - s) + "*" * (2 * s - 1))

    # Output -

    #     *
    #    ***
    #   *****
    #  *******
    # *********
    # *********
    #  *******
    #   *****
    #    ***
    #     *


def starsLadderUpSideDown(n, k=1):
    if k > n:
        return

    print("*" * k)
    starsLadderUpSideDown(n, k + 1)
    print("*" * (k - 1))

    # Output -

    # *
    # **
    # ***
    # ****
    # *****
    # ****
    # ***
    # **
    # *


def oneZeroTrianglePattern(n, k=1):
    def printFurther(x):
        if x == 0:
            print()
            return

        print((x + 1) % 2, end=" ")
        printFurther(x - 1)

    if k > n:
        return

    printFurther(k)
    oneZeroTrianglePattern(n, k + 1)

    # Output -

    # 0
    # 1 0
    # 0 1 0
    # 1 0 1 0
    # 0 1 0 1 0


def numbersMirrorPattern(n, k=1):
    def printRow1(x):
        if x == 0:
            return

        printRow1(x - 1)
        print(x, end="")

    def spaces(x):
        if x == 0:
            return

        print(" ", end="")
        spaces(x - 1)

    def printRow2(x):
        if x == 0:
            return

        print(x, end="")
        printRow2(x - 1)

    if k > n:
        return

    printRow1(k)
    spaces(2 * (n - k))
    printRow2(k)
    print()
    numbersMirrorPattern(n, k + 1)

    # Output -

    # 1        1
    # 12      21
    # 123    321
    # 1234  4321
    # 1234554321


def countingNumbers(n, k=1, x=1):
    def counter(a, b):
        if a == 0:
            return b

        b = counter(a - 1, b)
        print(b, end=" ")
        return b + 1

    if k > n:
        return

    counter(k, x)
    print()
    countingNumbers(n, k + 1, x + k)

    # Output -

    # 1
    # 2 3
    # 4 5 6
    # 7 8 9 10
    # 11 12 13 14 15


def charactarLadderRow(n):
    if n == 0:
        return

    charactarLadderRow(n - 1)
    print(chr(ord("A") + (n - 1)) * n)

    # Output -

    # A
    # BB
    # CCC
    # DDDD
    # EEEEE


def charactarLadderRowInverse(n):
    if n == 0:
        return

    print(chr(ord("A") + (n - 1)) * n)
    charactarLadderRowInverse(n - 1)

    # Output -

    # EEEEE
    # DDDD
    # CCC
    # BB
    # A


def charactarLadderCol(n):
    def printRow(k):
        if k == 0:
            return

        printRow(k - 1)
        print(chr(ord("A") + (k - 1)), end="")

    if n == 0:
        return

    charactarLadderCol(n - 1)
    printRow(n)
    print()

    # Output -

    # A
    # AB
    # ABC
    # ABCD
    # ABCDE


def charactarLadderColInverse(n):
    def printRow(k):
        if k == 0:
            return

        printRow(k - 1)
        print(chr(ord("A") + (k - 1)), end="")

    if n == 0:
        return

    printRow(n)
    print()
    charactarLadderColInverse(n - 1)

    # Output -

    # ABCDE
    # ABCD
    # ABC
    # AB
    # A


n = int(input())

# printNto1(n)

# print1toN(n)

# printEveryNumberTwiceExeptLargest(n)

# printNto1and1toN(n)

# print1toNandNto1(n)

# printDecimalToBinary(n)

# printStars(n, n)

# print1toNStars(n)

# printNto1Stars(n)

# printNto1LadderRow(n)

# print1toNLadderRow(n)

# print1ToNLadderCol(n)

# print1ToNLadderColInverse(n)

# printNto1LadderCol(n)

# printNto1LadderColInverse(n)

# triangleStars(n)

# triangleStarsInverse(n)

# triangleStarsUpSideDown(n)

# starsLadderUpSideDown(n)

# oneZeroTrianglePattern(n)

# numbersMirrorPattern(n)

# countingNumbers(n)

# charactarLadderRow(n)

# charactarLadderRowInverse(n)

# charactarLadderCol(n)

charactarLadderColInverse(n)
