

























                matrix.append(int(a[count_a])) 
                matrix.append(int(vectors[j][i]))
                print(a[count_a], end="")
                print(vectors[j][i], end="")
            count_a2 += 1
            count_first = False
            else:
            if count_a2 == count_tringle:
            out_A.append("("+i+")")
            out_A.append(i)
            out_Ael.append("("+i+")")
            out_Ael.append(i)
            print("+"+vectors[j][i]+"λ"+str(count_alfa), end="")
            print(vectors[j][i]+"λ"+str(count_alfa), end="")
        # занесение в словарь векторов
        A_str.append(str(i))
        None
        count_a += 1
        count_alfa += 1
        else:
        else:
        else:
        first = False
        for j in keys_list:
        i = str(i)
        if int(i) < 0:
        if int(i) < 0:
        if int(vectors[j][i]) > 0 and count_first is False:
        matrix.append(int(vectors[j][i]))
        opred_matrix_3x3(matrix)
        print(" ", j, end="")
        print("= ", end="")
        print("|", end="")
        print("Матрица не 3x3, определитель ищи сам")
        print("Например: p 3 -2 4\n"+" "*10+"g -2 1 3\n"+" "*10+"r 7 -4 1(при трёх измерениях)")
        print("Неверное количество символов!\nвведите ещё раз\n")
        print()
        print()
        print(vectors[j][i], end="")
        vectors[j[0]] = j[1:]
        x -= 1
    # Ввод
    # вывод всего
    # проверки
    # промежуточные штуки
    # сделаем чтобы отрицательные промежуточные штуки тоже в скобочки заключались
    # сделаем чтобы отрицательные числа в скобочки заключались
    A_el1 = A[0]*A[4]*A[8]
    A_el2 = A[1]*A[5]*A[6]
    A_el3 = A[3]*A[2]*A[7]
    A_el4 = A[6]*A[4]*A[2]
    A_el5 = A[1]*A[3]*A[8]
    A_el6 = A[0]*A[5]*A[7]
    A_str=[]
    Ael = [A_el1, A_el2, A_el3, A_el4, A_el5, A_el6]
    count_a += 1
    count_alfa = 1
    count_first = True
    count_tringle += 1
    elif 0 == 1:
    else:
    else:
    for i in A:
    for i in A_str:
    for i in Ael:
    for i in x:
    for j in keys_list:
    for j in keys_list:
    for j in vectors[i]:
    global opred_A, out_A
    if dim == 3:
    if first:
    if len(j) != dim+1:
    j = input("")
    j = j.split()
    matrix = []
    opred_A = (A[0]*A[4]*A[8]+A[1]*A[5]*A[6]+A[3]*A[2]*A[7]-A[6]*A[4]*A[2]-A[1]*A[3]*A[8]-A[0]*A[5]*A[7])
    opred_matrix_3x3(matrix)
    out_A = []
    out_Ael = []
    print(" ", i, end="")
    print(" =",a[count_a])
    print(")")
    print("= ", end="")
    print("{}*{}*{} + {}*{}*{} + {}*{}*{} - {}*{}*{} - {}*{}*{} - {}*{}*{} =".format(out_A[0], out_A[4], out_A[8], out_A[1], out_A[5], out_A[6], out_A[3], out_A[2], out_A[7], out_A[6], out_A[4], out_A[2], out_A[1], out_A[3], out_A[8], out_A[0], out_A[5], out_A[7]), end=" ")
    print("{}+{}+{}-{}-{}-{} = {}\n".format(out_Ael[0], out_Ael[1], out_Ael[2], out_Ael[3], out_Ael[4], out_Ael[5], opred_A))
    print("|")
    print("|", end="")
    print("Δ"+str(count_tringle))
    print("Введите название вектора базиса и его значения через пробелы")
    print("Матрица не 3x3, определитель ищи сам")
    print("⃗"+str(i),"= (",end="")
    print()
    return (A[0]*A[4]*A[8]+A[1]*A[5]*A[6]+A[3]*A[2]*A[7]-A[6]*A[4]*A[2]-A[1]*A[3]*A[8]-A[0]*A[5]*A[7])
# ------------ВВОД------------
# ------------Этап 1------------
# ------------Этап 2------------
# ------------Этап 3------------
# dim - dimentional - измерение
# Ввод
# просто треугольник
# треугольнички с чиселками
a = a.split()
a = input("По аналогии введите данные разлагаемого вектора\nНапример: a 25 -15 14\n")
count_a = 0
count_a = 1
count_a2 = 1
count_alfa = 1
count_tringle = 1
def opred(A):
def opred_matrix_3x3(A):
dim = int(input("Сколько измерений?\n"))
else:
first = True
for i in a[1:]:
for i in keys_list:
for i in x:
for i in x:
if dim == 3:
input()
keys_list = list(vectors.keys())
matrix = []
print("(число после λ - индекс λ)")
print(")\n")
print("1)Дано")
print("\nТреугольнички дельточки")
print("Δ")
print("⃗"+a[0],"= (",end="")
vectors = {} # словарь всех векторов
while count_tringle <= dim:
while x>0:
x = len(range(1,dim+1))
x = list(range(0,dim))