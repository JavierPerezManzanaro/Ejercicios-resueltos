import datetime
fecha1 = datetime.date.today()
fecha2 = datetime.date(2022, 1, 21)


print(f'{fecha1=}')
print(f'{fecha2=}')

print(fecha1 == fecha2)
print(fecha1 != fecha2)

if fecha1 == fecha2:
    print('Las fechas son iguales')


# otra forma menos eficiente

# import datetime

# d1 = datetime.datetime.today().strftime('%Y-%m-%d')
# d2 = datetime.datetime(2022, 1, 21).strftime('%Y-%m-%d')


# print(f'{d1=}')
# print(f'{d2=}')
# print(type(d1))

# if d1 == d2:
#     print('Las fechas son iguales')







