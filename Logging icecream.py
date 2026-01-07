
# icecream.info("Este es un mensaje de información")
# icecream.warning("Este es un mensaje de advertencia")
# icecream.error("Este es un mensaje de error")

from icecream import ic

def foo(i):
    return i + 333

ic(foo(123))


d = {'key': {1: 'one'}}
ic(d['key'][1])

class klass():
    attr = 'yep'
ic(klass.attr)


ic(1)

ic.disable()
ic(2)

ic.enable()
ic(3)
