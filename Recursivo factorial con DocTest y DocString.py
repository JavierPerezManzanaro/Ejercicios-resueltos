"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120
>>> recursivo.factorial(13)
6227020800
"""

class Recursivo:
    def factorial(self, number):
        if number == 0: return 1
        else: return number * self.factorial (number - 1)



recursivo = Recursivo()
print(recursivo.factorial(5))
print(recursivo.factorial(13))

#python3 -m doctest 'Recursivo factorial con DocTest y DocString.py'

if __name__ == "__main__":
    import doctest
    doctest.testmod()