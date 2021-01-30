from  functools import wraps
import time
import logging




  
class my_log(object):
    
    def __init__ (self, my_function):
        self.my_function=my_function
        logging.basicConfig(filename='{}.log'.format(self.my_function.__name__), level=logging.INFO)
    
    
    def __call__(self,*args, **kwargs):
        
        logging.info(
        'logging with arguments {} and kwargs {}'.format(args,kwargs))
        self.my_function(*args, **kwargs)
        print("el wrapper en logging empieza")
        



class my_time(object):
    def __init__(self,my_function):
        self.my_function=my_function
    
    def __call__(self,*args, **kwargs):
        t1=time.time()
        result = self.my_function(*args, **kwargs)
        tiempo=time.time()-t1
        print('{} ran in {} seconds'.format(self.my_function.__name__, tiempo))
        
        result
        print('el wrapper en la clase {} en time empieza'.format(self.my_function.__name__))
        
        
        


@my_time
def  display(edad, nombre):
    time.sleep(1)
    print (f"{nombre} tiene {edad} años")

@my_log
def  display(edad, nombre):
    time.sleep(1)
    print (f"{nombre} tiene {edad} años")

@my_log
def hola(numero):
    time.sleep(1)
    print(f"hola mundo, {numero}")
    
    
if __name__ =="__main__":
    hola (36)
    display(25,"Tom")

    
    