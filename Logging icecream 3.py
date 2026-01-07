from icecream import ic
import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)
def multiply(a, b):
    result = a * b
    ic(result)
    #logging.debug(f'Result: {result}')
    return result
multiply(2, 3)
