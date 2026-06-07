# Check numbers from 2 to 100
for num in range(2, 101):

    is_prime = True

    # Check divisibility
    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")