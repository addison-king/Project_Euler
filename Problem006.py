"""
Brandyn Gilbert
    Tue Mar 24 08:14:47 2020
    Project Euler
    Problem 6
"""
#PLAN
# =============================================================================
# # The sum of the squares of the first ten natural numbers is,
#
# # 12+22+...+102=385
# # The square of the sum of the first ten natural numbers is,
#
# # (1+2+...+10)2=552=3025
# # Hence the difference between the sum of the squares of the first ten natural
# #     numbers and the square of the sum is 3025−385=2640.
#
# # Find the difference between the sum of the squares of the first one hundred
# #     natural numbers and the square of the sum.
# =============================================================================


def main():
    print()
    sums = sum_of_squares()
    squared = squared_sum()
    final = squared - sums
    print(final)

def sum_of_squares():
    print()
    i = 0
    num_sum = 0
    while i < 100:
        i += 1
        num_sum += i**2
    return(num_sum)

def squared_sum():
    print()
    i = 0
    num_sum = 0
    while i < 100:
        i += 1
        num_sum += i
    squared = num_sum**2
    return squared

if __name__ == "__main__":
    main()
