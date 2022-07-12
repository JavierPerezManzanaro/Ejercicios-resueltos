# Hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo


def make_repeater_of(n):  # * 1 regla

    def repreater(string):  # * 2 regla
        assert type(string) == str, "Solo se pueden usar cadenas"
        return n * string

    return repreater  # * 3 regla




def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola '))


if __name__ == '__main__':
    run()