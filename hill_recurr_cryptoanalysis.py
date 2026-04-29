import numpy as np


# file_input = input("Введите название файла с шифртекстом: ")
# file_plain = input("Введите название файла с частью открытого текста: ")
file_input = "ciphertext_hill_recurr.txt"
file_plain = "plaintext_hill_recurr.txt"

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


