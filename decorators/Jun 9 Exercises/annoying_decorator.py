def annoying_decorator(function):
    def wrapper():
        greeting = function()
        if greeting == 'Hi':
            return f"Don't use Hi with me, please!"
        else:
            return f'Hello, Sir.'

    return wrapper


@annoying_decorator
def greetings():
    return "Hi"


if __name__ == '__main__':
    print(greetings())
