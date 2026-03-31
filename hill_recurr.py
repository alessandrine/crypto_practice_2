import numpy as np
from math import gcd

def cofactor_matr(matrix):
    minor_matr = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            minor = np.delete(matrix, i, axis=0) # delete i-string
            minor = np.delete(minor, j, axis=1) # delete j-column
            minor_matr[i, j] = (-1)**(i+j) * np.linalg.det(minor)
    return minor_matr.round().astype(int)


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


def hill_recurr(alphabet, text, key_str1, key_str2, type_e_d='e'):
    output = ""

    m = len(alphabet)
    key1 = np.matrix(key_str1)
    key2 = np.matrix(key_str2)
    if (not key_check(key1, m)) or (not key_check(key2, m)):
        return f"Введите обратимые по модулю {m} матрицы, перезапустив программу."

    size = np.shape(key1)[0]
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

    k = 0
    key_prev = None
    key_prev_prev = None

    for vect in text_array:
        k += 1

        if k == 1:
            key = key1
        elif k == 2:
            key = key2
        else:
            key = (key_prev * key_prev_prev) % m

        if type_e_d == 'd':
            det = int(np.round(np.linalg.det(key))) % m
            inv_det = pow(det, -1, m)
            adjoint_matr = np.transpose(cofactor_matr(key))
            key_inv = (inv_det * adjoint_matr) % m

            result = (key_inv * vect) % m
            output += to_letters(result, ord(alphabet[0]))
        elif type_e_d == 'e':
            result = (key * vect) % m
            output += to_letters(result, ord(alphabet[0]))

        key_prev_prev = key_prev
        key_prev = key

    return output


alph_hr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text_hr = input(
    "Введите в качестве обрабатываемого текста\nпоследовательность латинских символов\nв верхнем регистре:\n")
key1_hr = input(
    f"Введите в качестве 1-го ключа\nквадратную матрицу, обратимую по модулю {len(alph_hr)},\nв формате 'x11 x12 ... x1n;x21 x22 ... x2n; ...':\n")
key2_hr = input("Аналогично введите 2-ю ключевую матрицу:\n")
type_e_d_hr = input(
    "Выберите режим: чтобы произвести зашифрование (encryption),\nвведите «e» без кавычек; для расшифрования (decryption)\n– «d» аналогично: ")
print(hill_recurr(alph_hr, text_hr, key1_hr, key2_hr, type_e_d_hr))
