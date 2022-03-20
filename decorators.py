import time
import dis


def timer(function):
    def wrapper(*args, **kwargs) -> None:
        start = time.perf_counter()
        value = function(*args, **kwargs)
        end = time.perf_counter()
        print(f"Timer for {function.__name__}: {end - start}")
        return value

    return wrapper


def disassembler(function):
    def wrapper(*args, **kwargs) -> None:
        dis.dis(function)
        rv = function(*args, **kwargs)
        return rv

    return wrapper
