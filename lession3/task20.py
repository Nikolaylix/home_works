word = input('Введите слово: ').upper()
Eng = {'1':'A, E, I, O, U, L, N, S, T, R',
       '2':'D, G',
       '3':'B, C, M, P',
       '4':'F, H, V, W, Y',
       '5':'K',
       '8':'J, X',
      '10':'Q, Z'}

result = 0
for i in word:
    for j in Eng.keys():
        if i in Eng[j]:
            result += int(j)
            break

print(result)