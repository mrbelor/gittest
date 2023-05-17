# эта программа вычисляет разложение вектора "а" в трёхмерном базисе
print("Эта программа вычисляет разложение вектора \"а\" в трёхмерном базисе\nv.0.2.0(After Armageddon)")
base = []

first = True
while True:
    # ввод
    if first:
        print("\nВ", end = "")
    else:
        print("\nЕщё раз в", end = "")
    base = input("ведите название всех трёх вектов базиса и его значения подряд через пробелы\nНапример: p 3 -2 4 g -2 1 3 r 7 -4 1\n")
    base = base.split()
    print()
    
    
    # проверка базиса
    if len(base) != 12:
        print("Неверное количество символов!")
        continue
        first = False
    
    # ввод разлагаемого вектора
    first = True
    while True:
        if first:
            print("По аналогии ", end = "")
        else:
            print("Ещё раз ", end = "")
        a = input("введите данные разлагаемого вектора\nНапример: a 25 -15 14\n") 
        a = a.split()
        print()
        
        # проверка разлагаемого вектора
        if len(a) != 4:
            print("Неверное количество символов!")
            first = False
        else:
            break
            
    # ---------------------Дано---------------------
    print("Вы ввели:")
    print("⃗{} = ({}; {}; {})".format(base[0], base[1], base[2], base[3]))
    print("⃗{} = ({}; {}; {})".format(base[4], base[5], base[6], base[7]))
    print("⃗{} = ({}; {}; {})".format(base[8], base[9], base[10], base[11]))
    print("⃗{} = ({}; {}; {})\n".format(a[0], a[1], a[2], a[3]))
    
    print("Проверьте правильность")
    run = True
    while run:
        again = input("1)Да, всё правильно\n2)Начать сначала\n(1/2)\n")
        if again == "1":
            break
        elif again == "2":
            run = False
        else:
            print("Неккоректный ввод!\nНадо ввести либо 1 либо 2")
    else:
        continue

    # ---------------Этап1--------------------------
    print("Этап1")
    
    # преобразования
    base_out1 = []
    for i in base:
        if i.isdigit():

            # чтобы 1 исчезали
            if i == "1":
                j = ""
            elif i == "-1":
                j = "-"
            else:
                j = i

            # чтобы у положительных был "+"
            if int(i) > 0:
                base_out1.append("+"+j)
            else:
                base_out1.append(j)
        else:
            base_out1.append(i)

    # вывод
    print("{}λ₁{}λ₂{}λ₃ = {}".format(base[1], base_out1[2], base_out1[3], a[1]))
    print("{}λ₁{}λ₂{}λ₃ = {}".format(base[5], base_out1[6], base_out1[7], a[2]))
    print("{}λ₁{}λ₂{}λ₃ = {}\n".format(base[9], base_out1[10], base_out1[11], a[3]))

    # ---------------Этап2--------------------------
    print("Этап2\nТреугольнички дельточки")

    # выравнивание пробелами
    base_out2 = []
    for i in base:
        if i.isdigit():
            # в положительных числах
            if int(i) > -1:
                if int(i) > 9:
                    base_out2.append(" "+i)
                else:
                    base_out2.append("  "+i)
            # в отрицательных числах
            else:
                if int(i) < -9:
                    base_out2.append(i)
                else:
                    base_out2.append(" "+i)
        # в буквах
        else:
            base_out2.append(i)

    # всё в матрицу
    mtx = []
    j = [1, 5, 9, 2, 6, 10, 3, 7, 11]
    for i in j:
        mtx.append(base_out2[i])

    print(" |{};{};{}|\nΔ|{};{};{}|\n |{};{};{}|".format(mtx[0], mtx[1], mtx[3], mtx[4], mtx[5], mtx[6], mtx[7], mtx[8]))
break