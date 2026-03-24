import numpy as np
from math import gcd

'''
Гарантируется, что ключ задан верно, т.е. это матрица NxN
с числовыми значениями по модулю 26.
Осталось проверить, обратима ли ключевая матрица.
Её определитель (det) не должен быть равен 0 и НОД(det, m) == 1.
'''


def key_check(matr, m):
    det = np.linalg.det(matr)
    if det != 0:
        if gcd(int(det), m) == 1:
            return True
    return False


def to_letters(matr, ord_first_let):
    out = ""
    n = np.size(matr)
    for i in range(n):
        out += chr(matr.item((i, 0)) + ord_first_let)
    return out


def hill(alphabet, text, key_str, type_e_d='e'):
    output = ""

    m = len(alphabet)
    key = np.matrix(key_str)
    if not key_check(key, m):
        return f"Введите обратимую по модулю {m} матрицу."

    size = np.shape(key)[0]
    cnt = 0
    text_array = list()
    temp = ""
    for symb in text:
        cnt += 1
        if not (65 <= ord(symb) <= 90):
            return "Пожалуйста, в качестве обрабатываемого текста введите последовательность латинских символов заглавными буквами."
        if cnt <= size:
            temp = temp + str(ord(symb) - ord(alphabet[0])) + ';'
        if cnt == size:
            temp = temp.strip(';')
            num_temp = np.matrix(temp)
            text_array.append(num_temp)
            temp = ""
            cnt = 0

    for vect in text_array:
        if type_e_d == 'e':
            y = key * vect % m
            output += to_letters(y, ord(alphabet[0]))
        elif type_e_d == 'd':
            x = (np.linalg.inv(key).round() * vect % m).astype(int)
            output += to_letters(x, ord(alphabet[0]))
        else:
            return "Пожалуйста, выберите режим зашифрования или расшифрования, перезапустив программу."
    return output


alph_h = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text_h = input(
    "Введите в качестве обрабатываемого текста\nпоследовательность латинских символов\nв верхнем регистре:\n")
key_h = input(
    f"Введите в качестве ключа\nквадратную матрицу, обратимую по модулю {len(alph_h)},\nв формате 'x11 x12 ... x1n;x21 x22 ... x2n; ...':\n")
type_e_d_h = input(
    "Выберите режим: чтобы произвести зашифрование (encryption),\nвведите «e» без кавычек; для расшифрования (decryption)\n– «d» аналогично: ")
print(hill(alph_h, text_h, key_h, type_e_d_h))
