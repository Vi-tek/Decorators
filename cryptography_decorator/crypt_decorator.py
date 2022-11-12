from functools import wraps


class CryptDecorator:
    def __init__(self, cryptographic_algorithm, *args, **kwargs):
        self.crypt_alg = cryptographic_algorithm
        self.args = args
        self.kwargs = kwargs

    def __call__(self, method_instance):
        @wraps(method_instance)
        def wrapper(*args, **kwargs):
            if (rv := method_instance(*args, **kwargs)) is not None:
                return self.crypt_alg(self.__serialize(rv), *self.args, **self.kwargs)

        return wrapper

    @staticmethod
    def __serialize(input_stream) -> bytes:
        if not isinstance(input_stream, bytes):
            return bytes(str(input_stream).encode("utf-8"))
        return input_stream
