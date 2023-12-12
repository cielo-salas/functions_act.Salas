def smallest_factor(n):
    for i in range(2, n + 1):  # i is the factor of n(input)
        if n % i == 0:
            return i  # it will return i if the remainder is 0


def get_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

while True:
    print("\nWhat operation you want to do?:"
          "\nChoose from the following:"
          "\n[1] Find the smallest factor of a number."
          "\n[2] Find prime numbers in a range."
          "\n\nIf you want to exit press [0]")

    choice = int(input("\nEnter your choice: "))
    if choice == 0:
        print("Program terminated.")
        break
    if choice == 1:
        number = int(input("Enter an integer number >= 2:"))
        result = smallest_factor(number)

        print(f"The smallest factor of {number} other than 1 is {result}.")


    elif choice == 2:
        start_num = int(input("Enter a number [start]: "))
        if start_num < 0:
            print("Enter a non-negative number.")
            continue
        end_num = int(input("Enter a number [end]: "))
        if end_num < 0:
            print("Enter a non-negative number.")
            continue
        if end_num < start_num:
            print("Enter a number greater than [start].")
            continue

        else:
            prime_numbers = get_primes_in_range(start_num, end_num)
            print("Prime numbers between", start_num, "and", end_num, "are:", prime_numbers)

    else:
        print("Invalid choice. Please enter a valid option.")

    import time
    time.sleep(2)