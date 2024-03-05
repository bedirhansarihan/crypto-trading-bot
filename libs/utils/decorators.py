from time import time

def timer(func):
    def time_wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return time_wrapper



def create_buy_sell_signal(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
