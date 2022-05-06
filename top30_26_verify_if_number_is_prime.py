# Start a loop from value 2(k) up to (number / 2)
# If the number is perfectly divisible by k, then the number is non – prime.
# If the number is not perfectly divisible except for 1 and by itself, then the number is prime.


def verifyPrime(number):
    k = 2
    while k < len(number):
        if number % k == 0:
            print("not prime")
            return
    print("prime")

