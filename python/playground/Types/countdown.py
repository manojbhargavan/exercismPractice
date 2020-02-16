import sys


def factorial(number):
    fact = 1
    for i in range(int(number)):
        fact *= (i + 1)

    return fact


if __name__ == "__main__":
    result = factorial(sys.argv[1])
    print(result)
