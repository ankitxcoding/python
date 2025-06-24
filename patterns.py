def stars(n):
    for i in range(n):
        print("*" * n)

    # Output -

    # *****
    # *****
    # *****
    # *****
    # *****


def starsLadder(n):
    for i in range(n):
        print("*" * (i + 1))

    # Output -

    # *
    # **
    # ***
    # ****
    # *****


def starsLadderInvert(n):
    for i in range(n):
        print("*" * (n - i))

    # Output -

    # *****
    # ****
    # ***
    # **
    # *


def numbers1toNLadderRow(n):
    for row in range(n):
        for col in range(row + 1):
            print(col + 1, end="")
        print()

    # Output -

    # 1
    # 12
    # 123
    # 1234
    # 12345


def numbers1toNLadderRowInvert(n):
    for row in range(n):
        for col in range(n - row):
            print(col + 1, end="")
        print()

    # Output -

    # 12345
    # 1234
    # 123
    # 12
    # 1


def numbers1toNLadderCol(n):
    for row in range(n):
        for col in range(row + 1):
            print(row + 1, end="")
        print()

    # Output -

    # 1
    # 22
    # 333
    # 4444
    # 55555


def numbers1toNLadderColInvert(n):
    for row in range(n):
        for col in range(n - row):
            print(n - row, end="")
        print()

    # Output -

    # 55555
    # 4444
    # 333
    # 22
    # 1


def triangleStars(n):
    for row in range(n):
        for spaces in range(n - row - 1):
            print(" ", end="")
        for col in range(2 * row + 1):
            print("*", end="")
        print()

    # Output -

    #     *
    #    ***
    #   *****
    #  *******
    # *********


def triangleStarsInvert(n):
    for row in range(n):
        for spaces in range(row):
            print(" ", end="")
        for col in range(2 * (n - row) - 1):
            print("*", end="")
        print()

    # Output -

    # *********
    #  *******
    #   *****
    #    ***
    #     *


def triangleStarsUpSideDown(n):
    for row in range(n):
        for spaces in range(n - row - 1):
            print(" ", end="")
        for col in range(2 * row + 1):
            print("*", end="")
        print()
    for row in range(n):
        for spaces in range(row):
            print(" ", end="")
        for col in range(2 * (n - row) - 1):
            print("*", end="")
        print()

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


def starsLdderUpSideDown(n):
    for i in range(2 * n):
        if i < n:
            print("*" * (i + 1))
        else:
            print("*" * (2 * n - 1 - i))

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


def oneZeroTrianglePattern(n):
    for row in range(n):
        for col in range(row + 1):
            print(((row + col) + 1) % 2, end="  ")
        print("\n")

    # Output -

    # 1

    # 0  1

    # 1  0  1

    # 0  1  0  1

    # 1  0  1  0 1


def numbersMirrorPattern(n):
    for row in range(n):
        for col in range(row + 1):
            print(col + 1, end="")
        for spaces in range(2 * (n - row - 1)):
            print(" ", end="")
        for col in range(row + 1, 0, -1):
            print(col, end="")
        print()

    # Output -

    # 1        1
    # 12      21
    # 123    321
    # 1234  4321
    # 1234554321


def numberCountingPattern(n):
    count = 1
    for row in range(n):
        for col in range(row + 1):
            print(count, end="  ")
            count += 1
        print("\n")

    # Output -

    # 1

    # 2  3

    # 4  5  6

    # 7  8  9  10

    # 11  12  13  14  15


def charactarLadderCol(n):
    for row in range(n):
        for col in range(row + 1):
            print(chr(ord("A") + col), end="")
        print()

    # Output -

    # A
    # AB
    # ABC
    # ABCD
    # ABCDE


def charactarLadderColInvert(n):
    for row in range(n):
        for col in range(n - row):
            print(chr(ord("A") + col), end="")
        print()

    # Output -

    # ABCDE
    # ABCD
    # ABC
    # AB
    # A


def charactarLadderRow(n):
    for row in range(n):
        for col in range(row + 1):
            print(chr(ord("A") + row), end="")
        print()

    # Output -

    # A
    # BB
    # CCC
    # DDDD
    # EEEEE


def charactarLadderRowInvert(n):
    for row in range(n):
        for col in range(n - row):
            print(chr(ord("A") + row), end="")
        print()

    # Output -

    # AAAAA
    # BBBB
    # CCC
    # DD
    # E


def charactarTrianglePattern(n):
    for row in range(n):
        for spaces in range(n - row):
            print(" ", end="")
        for col in range(row + 1):
            print(chr(ord("A") + col), end="")
        for col in range(row, 0, -1):
            print(chr(ord("A") + (col - 1)), end="")
        print()


def charactarLadderMix(n):
    for row in range(n):
        for col in range(row + 1, 0, -1):
            print(chr(ord("A") + (n - col)), end="  ")
        print("\n")

    # Output -

    # E

    # D  E

    # C  D  E

    # B  C  D  E

    # A  B  C  D  E


def hollowDimongStars(n):
    for row in range(n):
        for col in range(n - row):
            print("*", end="")
        for spaces in range(2 * row):
            print(" ", end="")
        for col in range(n - row):
            print("*", end="")
        print()

    for row in range(n):
        for col in range(row + 1):
            print("*", end="")
        for spaces in range(2 * (n - row - 1)):
            print(" ", end="")
        for col in range(row + 1):
            print("*", end="")
        print()

    # Output -

    # **********
    # ****  ****
    # ***    ***
    # **      **
    # *        *
    # *        *
    # **      **
    # ***    ***
    # ****  ****
    # **********


def hollowDimongStarsInvert(n):
    for row in range(n):
        for col in range(row + 1):
            print("*", end="")
        for spaces in range(2 * (n - row - 1)):
            print(" ", end="")
        for col in range(row + 1):
            print("*", end="")
        print()

    for row in range(n):
        for col in range(n - row - 1):
            print("*", end="")
        for spaces in range(2 * (row + 1)):
            print(" ", end="")
        for col in range(n - row - 1):
            print("*", end="")
        print()

    # Output -

    # *        *
    # **      **
    # ***    ***
    # ****  ****
    # **********
    # ****  ****
    # ***    ***
    # **      **
    # *        *


def hollowStars(n):
    for row in range(n):
        for col in range(n):
            if row == 0 or col == 0 or row == n - 1 or col == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Output -

    # *****
    # *   *
    # *   *
    # *   *
    # *****


def theUltimateMatrixPattern(n):
    for row in range(2 * n - 1):
        for col in range(2 * n - 1):
            x = n - (min(row, col, 2 * (n - 1) - row, 2 * (n - 1) - col))
            print(x, end=" ")
        print()

    # Output -

    # 5 5 5 5 5 5 5 5 5
    # 5 4 4 4 4 4 4 4 5
    # 5 4 3 3 3 3 3 4 5
    # 5 4 3 2 2 2 3 4 5
    # 5 4 3 2 1 2 3 4 5
    # 5 4 3 2 2 2 3 4 5
    # 5 4 3 3 3 3 3 4 5
    # 5 4 4 4 4 4 4 4 5
    # 5 5 5 5 5 5 5 5 5


n = int(input())  # All outputs are for the n = 5

# stars(n)

# starsLadder(n)

# starsLadderInvert(n)

# numbers1toNLadderRow(n)

# numbers1toNLadderRowInvert(n)

# numbers1toNLadderCol(n)

# numbers1toNLadderColInvert(n)

# triangleStars(n)

# triangleStarsInvert(n)

# triangleStarsUpSideDown(n)

# starsLdderUpSideDown(n)

# oneZeroTrianglePattern(n)

# numbersMirrorPattern(n)

# numberCountingPattern(n)

# charactarLadderCol(n)

# charactarLadderColInvert(n)

# charactarLadderRow(n)

# charactarLadderRowInvert(n)

# charactarTrianglePattern(n)

# charactarLadderMix(n)

# hollowDimongStars(n)

# hollowDimongStarsInvert(n)

# hollowStars(n)

theUltimateMatrixPattern(n)
