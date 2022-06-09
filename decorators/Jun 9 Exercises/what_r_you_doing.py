def verbose(func):
    def wrapper(a, b):
        result = func(a, b)
        return f'sum_two invoked ({a},{b}) -> {result} '

    return wrapper


@verbose
def sum_two(a, b):
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 3))
