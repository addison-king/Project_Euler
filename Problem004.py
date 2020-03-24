"""
Brandyn Gilbert
    Tue Mar 24 11:06:40 2020
    Project Euler
    Problem 4
"""
#PLAN
# =============================================================================
# # Problem 4
# # A palindromic number reads the same both ways. The largest palindrome made
# #     from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# # Find the largest palindrome made from the product of two 3-digit numbers.
# =============================================================================


def main():
    i = 1
    j = 1
    largest_pali = 0
    while i < 1000:
        while j < 1000:
            total = i * j
            str_total = str(total)
            len_total = len(str_total)
            if str_total[::-1] == str_total and len_total > 1:
                if total > largest_pali:
                    largest_pali = total
            j += 1
        i += 1
        j = 1
    print(largest_pali)

if __name__ == "__main__":
    main()
