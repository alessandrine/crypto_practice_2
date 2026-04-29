import numpy as np

def cofactor_matr(matrix):
    minor_matr = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            minor = np.delete(matrix, i, axis=0) # delete i-string
            minor = np.delete(minor, j, axis=1) # delete j-column
            minor_matr[i, j] = (-1)**(i+j) * np.linalg.det(minor)
    return minor_matr.round().astype(int)


def to_str_for_matr(x):
    res_str_arr = []
    for string in x:
        res_str_arr.append(" ".join([str(i) for i in string]))
    res_str = ";".join(res_str_arr)
    a = np.matrix(res_str)
    return a.T

def to_str_from_matr(x):
    res_str_arr = []
    for string in x:
        res_str_arr.append(" ".join([str(i) for i in string]))
    res_str = ";".join(res_str_arr)
    return res_str

# file_input = input("Введите название файла с шифртекстом: ")
# file_plain = input("Введите название файла с частью открытого текста: ")
file_input = "ciphertext_hill.txt"
file_plain = "plaintext_hill.txt"

with open(file_input, 'r', encoding='utf-8') as f_input:
    ciphertext = f_input.readline().strip()
print(ciphertext, len(ciphertext)) # число 15 имеет делители 15, 5, 3, 1
with open(file_plain, 'r', encoding='utf-8') as f_plain:
    plaintext = f_plain.readline().strip()
print(plaintext, len(plaintext)) # 25 данных символов хватает на проверку гипотезы с делителями 3 и 5
'''================== ПРЕДПОЛОЖЕНИЕ: КЛЮЧ 3х3 ====================='''
print("\nДля ключа 3х3:")
x1 = [[] for i in range(3)]
y1 = [[] for i in range(3)]
for cnt in range(9):
    x1[cnt // 3].append(ord(plaintext[cnt]) - ord('A'))
    y1[cnt // 3].append(ord(ciphertext[cnt]) - ord('A'))
result = [f'K * {x1[j]}^T == {y1[j]}^T' for j in range(3)]
print(*result, sep='\n')
print("Вычисление ключевой матрицы. Всё по модулю 26")
k1 = np.matrix("15 0 2;10 12 24;1 14 23")
p1_det = int(np.round(np.linalg.det(k1))) % 26
print(f"Определитель матрицы для нахождения K11-13 равен: {p1_det}")
'''Ввиду необратимости по модулю детерминанта матрицы коэффициентов,
делаем вывод о том, что ключ не может быть 3x3.'''
'''================== ПРЕДПОЛОЖЕНИЕ: КЛЮЧ 5х5 ====================='''
print("\nДля ключа 5х5:")
x1 = [[] for i in range(5)]
y1 = [[] for i in range(5)]
for cnt in range(25):
    x1[cnt // 5].append(ord(plaintext[cnt]) - ord('A'))
    y1[cnt // 5].append(ord(ciphertext[cnt]) - ord('A'))
result = [f'K * {x1[j]}^T == {y1[j]}^T' for j in range(5)]
print(*result, sep='\n')
print("Вычисление ключевой матрицы. Всё по модулю 26")
'''Составление матрицы коэффициентов'''
print(p1_T:=to_str_for_matr(x1))
p1_det = int(np.round(np.linalg.det(p1_T))) % 26
print("Детерминант матрицы коэффициентов: ", p1_det) # 25 обратимо по модулю 26
'''Расчёт обратной матрицы коэффициентов'''
inv_det = pow(p1_det, -1, 26)
adjoint_matr = np.transpose(cofactor_matr(p1_T))
p1_inv = (inv_det * adjoint_matr) % 26
'''Расчёт ключа как K = C^T * (P^T)^(-1)'''
key = to_str_for_matr(y1) * p1_inv % 26
print("Ключ 5х5:\n", key)
print("Ключ 5х5 в формате строки:\n", to_str_from_matr(key))

# key = "2 3 1 5 4;3 5 2 1 1;1 2 4 3 2;5 1 3 6 1;4 1 2 1 7"


