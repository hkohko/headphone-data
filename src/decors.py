from pathlib import Path

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


def create_dir(path: Path):
    def decorator(func):
        def wrapper(*args):
            if not Path(path).exists():
                Path(path).mkdir()
            try:
                return func(args)
            except TypeError:
                return func()

        return wrapper

    return decorator
