"""
Brandyn Gilbert
    Tue Mar 24 11:33:49 2020
    Project Euler
    Problem 16
"""
#PLAN

# =============================================================================
# # Problem 16
# # 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# # What is the sum of the digits of the number 2^1000?
# =============================================================================

def main():

    value = 2 ** 1000
    str_value = str(value)
    total = 0
    for i in str_value:
        total += int(i)
    print(total)

if __name__ == "__main__":
    main()
