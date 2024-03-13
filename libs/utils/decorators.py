from time import time
from libs.utils.validators import validate_parameters_info


def create_buy_sell_signal(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

def timer(func):
    def time_wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return time_wrapper


def validate_param_info(cls):
    validate_parameters_info(cls.__PARAMETERS_INFO__)
    return cls


