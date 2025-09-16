

def is_prime(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():

    numbers = list(range(1, 101))


    prime_numbers = []

    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)


    print("Prime numbers between 1 and 100:")
    print(prime_numbers)

if __name__ == "__main__":
    main()
