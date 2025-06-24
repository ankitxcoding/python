def recursiveDecimalToBinary(n):
    if n == 0:
        return

    recursiveDecimalToBinary(n // 2)
    print(n % 2, end="")


n = int(input())

recursiveDecimalToBinary(n)


# recursive with return type instead of printing.

# def recursiveDecimalToBinary(n):
#     if n == 0:
#         return "0"
#     return _recursiveHelper(n)

# def _recursiveHelper(n):
#     if n == 0:
#         return ""
#     return _recursiveHelper(n // 2) + str(n % 2)

# # Example usage
# n = int(input("Enter a number: "))
# binary = recursiveDecimalToBinary(n)
# print(binary)
