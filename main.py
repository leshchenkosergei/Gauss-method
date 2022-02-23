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


def get_minor(matrix, m, k):
    minor = []
    for i in range(len(matrix)):
        if i != m:
            str = []
            for j in range(len(matrix)):
                if j != k:
                     str.append(matrix[i][j])
            minor.append(str)
    return minor


def get_det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = 0
        swap = 1
        for i in range(len(matrix)):
            det = det + swap * matrix[0][i] * get_det(get_minor(matrix, 0, i))
            swap = swap * (-1)
    return det


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
    print("Введите числа через пробел, по оконачанию ввода строки нажмите enter : ")
    while len(matrix) != n:
        line = input()
        try:
            str = list(map(float, line.split()))
        except ValueError:
            print("Ошибка, в строке некорректный элемент, повторите попытку")
            continue
        if len(str) != (n + 1):
            print("Ошибка, строка неверной длины, повторите попытку")
            continue
        matrix.append(str)
    return matrix


def transform(matrix):
    swap = 1
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
            swap = swap * (-1)

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

def get_discrepancy(matrix):
    result = get_roots(matrix)
    discrepancy = []
    for i in range(len(matrix)):
        res = 0
        for j in range(len(matrix)):
            res += result[j] * matrix[i][j]
        discrepancy.append(res - matrix[i][len(matrix)])
    return discrepancy

def main_fun():
    print("Введите \"1\" для ввода с клавиатуры, введите \"2\" для чтения из файла")
    num = input()
    if num == "1":
        matrix = keyboard_read()
        if get_det(matrix) == 0:
            print("Матрица несовместна")
            return
    print("Определитель матрицы равен: " + get_det(matrix).__str__())
    matrix = transform(matrix)
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
    result = get_roots(matrix)
    print("Вектор неизвестных:")
    for i in range(0, len(matrix)):
        print(result[i])
    discrepancy = get_discrepancy(matrix)
    print("Вектора невязок: ")
    for i in discrepancy:
        print(i)


about_lab()
main_fun()