# Write a function add(x: float, y: float) -> float that adds two numbers.

# Write a function multiply(x: float, y: float) -> float that multiplies two numbers.

# Write a function square(x: float) -> float that squares a number (hint: it must use multiply).

# Write a function add_squares(x: float, y: float) -> float that adds the squares of two numbers (hint: it must use both add and square).

x = 9
y = 4


def add(x: float, y: float) -> float:
    return x + y


def multiply(x: float, y: float) -> float:
    return x * y


def square(x: float) -> float:
    return multiply(x, x)


def add_squares(x: float, y: float) -> float:
    return add(square(x), square(y))


def main():
    print(add(x, y))
    print(multiply(x, y))
    print(square(x))
    print(add_squares(x, y))


if __name__ == "__main__":
    main()
