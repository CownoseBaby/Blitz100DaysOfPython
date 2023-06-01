statement = ""
for number in range(1,101):
    statement = f"{number}"
    if number % 3 == 0:
        statement = "Fizz"
    if number % 5 == 0:
        statement = "Buzz"
    if number % 3 == 0 and number % 5 == 0:
        statement = "FizzBuzz"
    print(statement)