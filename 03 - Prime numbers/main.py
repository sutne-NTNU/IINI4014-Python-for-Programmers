from math import sqrt
from time import time

start = time()

# 1000th prime number is 7919, so the quickest way i know to find the first 1000
# is to have a list then filter away all the numbers that arent prime
primes = list(range(2, 7919 + 1))
# remove all even numbers
primes = [n for n in primes if (n % 2 != 0 or n == 2)]
# now we just have to check against odd numbers
for i in range(3, int(sqrt(7907) + 1), 2):
    # filter away all numbers divisible by i
    primes = [n for n in primes if (n % i != 0 or n == i)]

end = time()

# printing results
print("primes:", primes)  # [1, 2, 3, 5, 7, 11, .... , 7877, 7879, 7883, 7901, 7907]
print("Time to calculate: %.5f seconds" % (end - start))  # 0.00389 seconds
print("Number of primes found:", len(primes))  # 1000
