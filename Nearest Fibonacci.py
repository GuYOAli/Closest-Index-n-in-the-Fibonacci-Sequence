
def fib(number):

    if number < 0:
        return "Invalid Input please try again."

    fib_numbers = [0, 1]
    first = 0
    second = 1

    sum = first + second

    while(sum <= number):

        # swap the values
        first, second = second, sum

        sum = first + second

        fib_numbers.append(sum)

    message = "It's Fibonacci" if number in fib_numbers else "It's Not Fibonacci"

    if abs(sum - number) >= abs(second - number):
        result = second
    else:
        result = sum

    return message, result


result = fib(4)

print(result)
