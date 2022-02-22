def about_lab():
    print("Лабораторная работа 1. «Решение системы линейных алгебраических уравнений СЛАУ»")
    print("Вариант: 11")
    print("Автор: Лещенко Сергей Дмитриевич P3223")
    print()

def keyboard_read():
    n = 0
    while True:
        try:
            n = int(input("Введите размерность матрицы (n<=20): "))
        except ValueError:
            print("Размерность может быть только натуральным числом меньшим или равным 20")
            continue
        if n <= 0 or n > 20:
            print("Размерность может быть только натуральным числом меньшим или равным 20")
            continue
        break
    matrix = []
    while len(matrix) != n:
        line = input("Введите числа через проблем: ")
        str = list(map(float, line.split()))
        matrix.append(str)
    return matrix

def main_fun():
    print("Введите \"1\" для ввода с клавиатуры, введите \"2\" для чтения из файла")
    num = input()
    if num == "1":
        print(keyboard_read())

about_lab()
main_fun()