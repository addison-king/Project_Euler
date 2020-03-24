"""
Brandyn Gilbert
    Tue Mar 24 08:48:28 2020
    Project Euler
    Problem 25
"""
#PLAN
# =============================================================================
# # The Fibonacci sequence is defined by the recurrence relation:
#
# # Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# # Hence the first 12 terms will be:
#
# # F1 = 1
# # F2 = 1
# # F3 = 2
# # F4 = 3
# # F5 = 5
# # F6 = 8
# # F7 = 13
# # F8 = 21
# # F9 = 34
# # F10 = 55
# # F11 = 89
# # F12 = 144
# # The 12th term, F12, is the first term to contain three digits.
#
# # What is the index of the first term in the Fibonacci sequence to contain
# #     1000 digits?
# =============================================================================


def main():

    fn1 = 1
    fn2 = 1
    fn3 = 0
    i = 2
    j = len(str(fn1))

    while j < 1000:
        fibbo = lambda x,y: x+y
        fn3 = fibbo(fn1, fn2)
        fn1 = fn2
        fn2 = fn3
        i += 1
        j = len(str(fn2))
        print(i,'::', fn2, '::', j)

    print('\n\n\n')
    print(i)


if __name__ == "__main__":
    main()
