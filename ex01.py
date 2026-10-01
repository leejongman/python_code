import time

def is_prime(number: int) -> bool:
    """Return True if number is a prime number, otherwise False."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3,number, 2):
        if number % divisor == 0:
            return False
    return True

def main():

    #prime number list
    start = time.time()
    time.sleep(1)  # Simulate some delay
    prime_numbers = []
    for num in range(1, 5001):
        if is_prime(num):
            prime_numbers.append(num)               

    print ("Prime numbers between 1 and 5000:", prime_numbers)
    end = time.time()
    print(f"Elapsed time: {end - start}")
    print(prime_numbers)   

if __name__ == "__main__":
    main()
