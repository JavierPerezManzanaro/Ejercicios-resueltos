def funcion(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
    
funcion('a', 'b', 'c', 'd', n=125, m=987)