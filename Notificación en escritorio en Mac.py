import os
title = 'Simulación para mac'
message = 'La simulación ha finalizado'
os.system("osascript -e 'display notification \"{}\" with title \"{}\"'".format(message, title))



def message(title, message): 
    #os.system('notify-send "'+title+'" "'+message+'"')
    os.system("osascript -e 'display notification \"{}\" with title \"{}\"'".format(message, title))



message('Título', 'Mensaje de notificación como función')

