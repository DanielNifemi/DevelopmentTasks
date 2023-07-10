def fibonacci_sum(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return sum(fib_sequence)


# Calculate the sum of the first 50 Fibonacci numbers
sum_of_fibonacci = fibonacci_sum(50)

print("Sum of the first 50 Fibonacci numbers:", sum_of_fibonacci)
