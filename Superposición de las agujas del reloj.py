from pprint import pprint

# Fuentes
# https://www.20minutos.es/gonzoo/noticia/5113039/0/cuantas-veces-dia-superponen-agujas-reloj-pregunta-entrevistas-trabajo/
# https://es.wikipedia.org/wiki/Matemáticas_en_la_esfera_del_reloj

minutos_dic = {}
minutos_dic_temp = {}

for minuto in range(0,60):
    # el 6 = 360/60
    angulo_minuto = 6*minuto
    # print(f'el minuto: {minuto} tiene el ángulo: {angulo_minuto}º')
    minutos_dic_temp = {angulo_minuto: minuto}
    minutos_dic = {**minutos_dic_temp, **minutos_dic}
    # pprint(minutos_dic)

for hora in range(0,12):
    # 30 = 360/12
    angulo_hora = 30*hora
    # print(f'la hora: {hora} tiene el ángulo: {angulo_hora}º')
    if angulo_hora in minutos_dic:
        print(f'A las {hora}:{minutos_dic[angulo_hora]} se superponen las agujas del reloj en los {angulo_hora}º')


#
