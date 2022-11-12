import hashlib
from crypt_decorator import CryptDecorator


def test_algorithm(message: bytes, shift: int = 21):
    rs: str = ""
    for x in message:
        rs += chr(x + shift)
    return rs


@CryptDecorator(test_algorithm, shift=1080)
def return_string(value: str):
    return value


@CryptDecorator(hashlib.sha1)
def return_string2():
    return "golden python"


if __name__ == '__main__':
    print(return_string("golden python"))
    print(return_string2().hexdigest())
