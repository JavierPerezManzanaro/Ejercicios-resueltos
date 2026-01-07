from icecream import install, ic
install()
ic.configureOutput(prefix='', includeContext=True)
import sys
from icecream import ic

ic.configureOutput(outputFunction=lambda *a: print(*a, file=sys.stderr))
def is_even(num):
    result = num % 2 == 0
    ic(result, num)
    return result
is_even(4)
is_even(5)

def sum_list(numbers):
    result = sum(numbers)
    ic(numbers, result)
    return result
sum_list([1, 2, 3, 4, 5])
