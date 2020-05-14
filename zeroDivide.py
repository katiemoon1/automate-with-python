def spam(divideBy):
  # try clause works around errors and if error occurs moves to the except clause
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')


print(spam(2))
print(spam(12))
# a ZeroDivisionError is thrown whenever you try to divide a number by zero
print(spam(0))
print(spam(1))
