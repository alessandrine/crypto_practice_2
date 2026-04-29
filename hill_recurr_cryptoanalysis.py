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

file_input = input("Введите название файла с шифртекстом: ")
file_plain = input("Введите название файла с частью открытого текста: ")
# file_input = "ciphertext_hill-2.txt"
# file_plain = "plaintext_hill-2.txt"
with open(file_input, 'r', encoding='utf-8') as f_input:
    ciphertext = f_input.readline().strip()
print(ciphertext, len(ciphertext)) # делители 44: 1, 2, 22, 4, 11, 44
with open(file_plain, 'r', encoding='utf-8') as f_plain:
    plaintext = f_plain.readline().strip()
print(plaintext, len(plaintext)) # 12 данных символов хватает на проверку гипотезы с делителем 2 (2 блока по 4 + доп. блок)
'''================== ПРЕДПОЛОЖЕНИЕ: КЛЮЧ 2х2 ====================='''
x1 = [[] for i in range(4)]
y1 = [[] for i in range(4)]
for cnt in range(8):
    x1[cnt // 2].append(ord(plaintext[cnt]) - ord('A'))
    y1[cnt // 2].append(ord(ciphertext[cnt]) - ord('A'))
result = [f'K{j+1} * {x1[j]}^T == {y1[j]}^T' for j in range(4)]
print(*result, sep='\n')


