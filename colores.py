""" Muestra todos los códigos ANSI de color posibles en la terminal """

# PARA QUE FUNCIONEN LOS COLORES EN EL TERMINAL INCLUÍDO EN WINDOWS
if __import__("platform").system() == "Windows": # si el Sistema Operativo es Windows
    kernel32 = __import__("ctypes").windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    del kernel32

# MUESTRA UNA TABLA DE COLORES EN LA TERMINAL CON SUS CORRESPONDIENTES CÓDIGOS ANSI
for estilo in range(10):
    for color_texto in range(30,38):
        codigo_ansi = ""
        for color_fondo in range(40,48):
            format = ';'.join([str(estilo), str(color_texto), str(color_fondo)])
            codigo_ansi += f"\33[{format}m {format} \33[0m"
        print(codigo_ansi)
    print()
