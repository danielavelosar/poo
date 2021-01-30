# Decorators
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

from  functools import wraps
import time
def my_log(my_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(my_function.__name__), level=logging.INFO)
    @wraps(my_function)
    def wrapper(*args, **kwargs):
        logging.info(
        'logging with arguments {} and kwargs {}'.format(args,kwargs))
        return my_function(*args, **kwargs)
    print("el wrapper en logging empieza")
    return wrapper



def my_time(my_function):
    @wraps(my_function)
    def wrapper(*args, **kwargs):
        t1=time.time()
        result = my_function(*args, **kwargs)
        tiempo=time.time()-t1
        print('{} ran in {} seconds'.format(my_function.__name__, tiempo))
        
        return result
    print('el wrapper en la función {} en time empieza'.format(my_function.__name__))
    return wrapper
    
    def my_log(my_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(my_function.__name__), level=logging.INFO)
    @wraps(my_function)
    def wrapper(*args, **kwargs):
        logging.info(
        'logging with arguments {} and kwargs {}'.format(args,kwargs))
        return my_function(*args, **kwargs)
    print("el wrapper en logging empieza")
    return wrapper



class my_time():
    def __init__(self,my_function):
        self.my_function=my_function
    @wraps(my_function)
    def wrapper(*args, **kwargs):
        t1=time.time()
        result = self.my_function(*args, **kwargs)
        tiempo=time.time()-t1
        print('{} ran in {} seconds'.format(self.my_function.__name__, tiempo))
        
        return result
    print('el wrapper en la clase {} en time empieza'.format(self.my_function.__name__))
    return wrapper


@my_log
@my_time
def  display(edad, nombre):
    time.sleep(1)
    print (f"{nombre} tiene {edad} años")

@my_log
@my_time
def hola(numero):
    time.sleep(1)
    print(f"hola mundo, {numero}")
    
    
if __name__ =="__main__":
    hola (36)
    display(25,"Tom")


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)