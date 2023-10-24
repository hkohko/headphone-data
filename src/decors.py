from constants import JSON_FILES


def write_result(filename: str):
    def decorator(func):
        def wrapper(*args):
            try:
                result = func(args)
            except TypeError:
                result = func()
            with open(JSON_FILES.joinpath(filename), "w") as file:
                file.write(result)

        return wrapper

    return decorator
