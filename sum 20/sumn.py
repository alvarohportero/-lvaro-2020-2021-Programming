# Session 1. Exercise 4
# CALCULATE THE SUM OF n
# 1 + 2+ 2+...20..n
# EXAMPLE WORKING


def sumn(n):
    res = 0
    for i in range(1, n + 1):
        res += 1
    return res


# the main program starts here
print("Sum of the first 20 first integers", sumn(20))
print("Sum of the 100, first integers", sumn(100))
