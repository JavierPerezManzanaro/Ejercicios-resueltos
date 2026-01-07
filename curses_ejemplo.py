import curses

def main(stdscr):
    # Inicializar el modo curses
    curses.curs_set(0)  # Ocultar cursor
    stdscr.clear()  # Limpiar la pantalla

    # Crear ventana
    height, width = stdscr.getmaxyx()  # Obtener tamaño de la terminal
    win = curses.newwin(height - 2, width - 2, 1, 1)  # Ventana

    # Configuración de colores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # Escribir mensaje
    win.addstr(0, 0, 'Presiona "q" para salir.', curses.color_pair(1))
    win.refresh()

    # Bucle principal
    while True:
        win.addstr(2, 0, 'Escriba algo: ', curses.color_pair(2))
        win.refresh()
        user_input = win.getstr(3, 0, 20).decode('utf-8')  # Leer entrada del usuario
        
        if user_input.lower() == 'q':
            break  # Salir del bucle si se presiona 'q'
        
        win.addstr(5, 0, f'Has escrito: {user_input}', curses.color_pair(1))
        win.refresh()
        win.clear()  # Limpiar ventana para la próxima entrada

    stdscr.addstr(height - 1, 0, 'Saliendo...') 
    stdscr.refresh()  
    stdscr.getch()  # Esperar una tecla antes de cerrar

curses.wrapper(main)
