def about_lab():
    print("Лабораторная работа 1. «Решение системы линейных алгебраических уравнений СЛАУ»")
    print("Вариант: 11")
    print("Автор: Лещенко Сергей Дмитриевич P3223")
    print()

def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

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


def transform(matrix):
    for i in range(len(matrix) - 1):

        max = abs(matrix[i][i])
        el_num = 0
        for j in range(i, len(matrix)):
            if abs(matrix[j][i]) > max:
                max = matrix[j][i]
                el_num = j

        if (max > abs(matrix[i][i])):
            row = matrix[i]
            matrix[i] = matrix[el_num]
            matrix[el_num] = row

        for k in range(i + 1, len(matrix)):
            с = matrix[k][i]/matrix[i][i]
            for j in range(i, len(matrix) + 1):
                matrix[k][j] = round(matrix[k][j] - с * matrix[i][j], 3)

    return matrix


def get_roots(matrix):
    result = [0] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        s = 0
        for j in range(i + 1, len(matrix)):
            s = s + matrix[i][j] * result[j]
        result[i] = round((matrix[i][len(matrix)] - s) / matrix[i][i], 3)
    return result


def main_fun():
    print("Введите \"1\" для ввода с клавиатуры, введите \"2\" для чтения из файла")
    num = input()
    if num == "1":
        matrix = transform(keyboard_read())
    str_matrix = ""
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            str_matrix = str_matrix + matrix[i][j].__str__()
            if get_count(matrix[i][j]) == 1:
                str_matrix = str_matrix + "   "
            elif get_count(matrix[i][j]) == 2:
                str_matrix = str_matrix + "  "
            else:
                str_matrix = str_matrix + " "
        str_matrix = str_matrix + '\n'
    print("Преобразованная матрица со столбцом B:")
    print(str_matrix)
    print()

about_lab()
main_fun()