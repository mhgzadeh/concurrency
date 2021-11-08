def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # print(f"{n} is not prime")
            return f"{n} not prime"
    # print(f"{n} is prime.")
    return f"{n} prime"


DEFAULT_NUMBERS = [12345623, 8735293749, 2349874298, 234872387, 560982348, 45989348,
                   2398754448, 498734343, 2309834, 45845472, 203490934, 394587] * 2000
