"""
Brandyn Gilbert
    Sat Mar 14 12:47:54 2020
    Project Euler
    Problem 3
"""
#PLAN
# =============================================================================
# # Largest prime factor
#
# # Problem 3
# # The prime factors of 13195 are 5, 7, 13 and 29.
#
# # What is the largest prime factor of the number 600851475143 ?
# =============================================================================


def main():
    factors = []
    prime_factors = []
    number = 13195
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)


    print(factors)
    for i in factors:
        if i != 1:
            print(i)
            for j in range(2, i-1):



if __name__ == "__main__":
    main()
