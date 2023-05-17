# -*- coding: utf8 -*- 
import math
#=====================defы=====================
# Доп утилиты
def opred_3x3(A):

    return (A[0]*A[4]*A[8]+A[1]*A[5]*A[6]+A[3]*A[2]*A[7]-A[6]*A[4]*A[2]-A[1]*A[3]*A[8]-A[0]*A[5]*A[7])
def opred_2x2(A):

    return (A[0]*A[3]-A[1]*A[2])
def opred_3x3_sol(A):
    # сделаем чтобы отрицательные числа в скобочки заключались
    A_str=[]
    for i in A:
        A_str.append(str(i))

    out_A = []
    for i in A_str:
        if int(i) < 0:
            out_A.append("("+i+")")
        else:
            out_A.append(i)
    # промежуточные штуки
    A_el1 = A[0]*A[4]*A[8]
    A_el2 = A[1]*A[5]*A[6]
    A_el3 = A[3]*A[2]*A[7]
    A_el4 = A[6]*A[4]*A[2]
    A_el5 = A[1]*A[3]*A[8]
    
    A_el6 = A[0]*A[5]*A[7]
    Ael = [A_el1, A_el2, A_el3, A_el4, A_el5, A_el6]
    # сделаем чтобы отрицательные промежуточные штуки тоже в скобочки заключались
    out_Ael = []
    for i in Ael:
        i = str(i)
        if int(i) < 0:
            out_Ael.append("("+i+")")
        else:
            out_Ael.append(i)
    # вывод всего
    return "{}*{}*{} + {}*{}*{} + {}*{}*{} - {}*{}*{} - {}*{}*{} - {}*{}*{} = {}+{}+{}-{}-{}-{} = {}".format(out_A[0], out_A[4], out_A[8], out_A[1], out_A[5], out_A[6], out_A[3], out_A[2], out_A[7], out_A[6], out_A[4], out_A[2], out_A[1], out_A[3], out_A[8], out_A[0], out_A[5], out_A[7], out_Ael[0], out_Ael[1], out_Ael[2], out_Ael[3], out_Ael[4], out_Ael[5], opred_3x3(A))
def opred_2x2_sol(A):
    # сделаем чтобы отрицательные числа в скобочки заключались
    A_str=[]
    for i in A:
        A_str.append(str(i))

    out_A = []
    for i in A_str:
        if int(i) < 0:
            out_A.append("("+i+")")
        else:
            out_A.append(i)
    # промежуточные штуки
    A_el1 = A[0]*A[3]
    A_el2 = A[1]*A[2]
    Ael = [A_el1, A_el2]
    # сделаем чтобы отрицательные промежуточные штуки тоже в скобочки заключались
    out_Ael = []
    for i in Ael:
        i = str(i)
        if int(i) < 0:
            out_Ael.append("("+i+")")
        else:
            out_Ael.append(i)
    # вывод всего
    return "{}*{} - {}*{} = {}-{} = {}".format(out_A[0], out_A[3], out_A[1], out_A[2], out_Ael[0], out_Ael[1], opred_2x2(A))
def convert(chislo, number_system, target_system): 
    #chislo(str); number_system(int);target_system(int) 
    i10 = int(str(chislo),number_system) 
    alfabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    result="" 
    while i10>0: 
        k = i10%target_system   #очередная цифра 
        result = alfabet[k]+result #приклеиваем спереди в соответствии с алфавитом 
        i10 = i10//target_system 
    return result
def socrat(n,m):
    k = math.gcd(n,m)
    return n//k, m//k
# Выборы
def choice1():
    default_or_not = 0
    quite_or_not = "y"
    while True:
        if quite_or_not == "y" or quite_or_not == "Y":
            x = input("Введите число\n") 
            y = int(input("В какой системе это число? (от 2 до 37)\n")) 
            if y >= 37: 
                print("\nТы щас серьёзно? 37?? Я ясно написал \"ДО 37\"\n")  #просто пасхалочка 
                continue 
            if not default_or_not:       #вопросы о выборе 
                default_or_not = int(input("1)Перевести в системы (2-16)\n2)Ввести собственный список систем от 2 до 37\n(1/2) ")) 
                if not(0<default_or_not<3): 
                    print("Число не соответстует интервалу. Либо 1 либо 2.") 
                    default_or_not = 0 
            else: 
                default_or_not = int(input("1)2-16\n2)Ввести свои системы\n3)Предыдущий введёный список систем\n(1/2/3) ")) 
            #результат от выбора--------------------------------------------------------------------
            if default_or_not == 1:     #выводит перевод в системы (2-16) 
                for i in range(2,17): 
                    print("В",i,"cc это",convert(x,y,i)) 
                z = list(range(2,17)) 
            elif default_or_not == 2:     #выводит перевод в заданные системы 
                z = input("В какие системы хотите первести? (>= 2 и <= 36)\nЧерез запятую, пробелы или точки\n") 
                z = z.replace(","," ") 
                z = z.replace("."," ") 
                z = z.split() 
                for i in z: 
                    print("В",i,"cc это",convert(x,y,int(i))) 
            elif default_or_not == 3:     #выводит перевод в заданные ранее системы 
                for i in z: 
                    print("В",i,"cc это",convert(x,y,int(i)))
            elif not(0<default_or_not<4): 
                print("Нужно было ввести цифру в соответствии с выбором") 
                default_or_not = 0 
        elif quite_or_not == "n" or quite_or_not == "N": 
            return 
        elif quite_or_not == "у":  #просто пасхалочка 
            print("\nЕсли что, \"y\" и \"n\" это yes или no\nА ты, как я вижу, забил на смысл и написал русскую \"у\"?\nБоже.. чел..") 
        else: 
            print("\nНадо ввести \"y\" (yes) или \"n\" (no)")   
        quite_or_not = input("Ещё раз? (y/n) ") 
def choice2_1():
    while True:
        A_str = input("\nВведите элементы матрицы 2x2 по книжному порядку через точки, запятые или пробелы (4 штуки)\nНапример: -1 -7 10 -1\n")
        A_str = A_str.replace(",", " ")
        A_str = A_str.replace(".", " ")
        A_str = A_str.split()
        # проверка 1
        if len(A_str) != 4:
            print("Вы ввели ошибочное количество элементов!")
            continue
        # проверка 2
        prov2 = ""
        for i in A_str:
            prov2 += i
        prov2 = prov2.replace("-", "")
        if not prov2.isdigit():
            print("В списке должны быть только цифры!")
            continue

        out_A = []
        for i in A_str:
            if int(i) < 0:
                out_A.append("("+i+")")
            else:
                out_A.append(i)
        # делаем матрицу int
        A=[]
        for i in A_str:
            A.append(int(i))
        opred_A = opred_2x2(A)
        print(opred_2x2_sol(A))
        print()
        return A, opred_A, out_A
def choice2_2():
    while True:
        A_str = input("\nВведите элементы матрицы по книжному порядку через точки,запятые или пробелы (9 штук)\nНапример: -1 -7 10 -1 8 8 9 1 1\n")
        A_str = A_str.replace(",", " ")
        A_str = A_str.replace(".", " ")
        A_str = A_str.split()
        # проверка 1
        if len(A_str) != 9:
            print("Вы ввели ошибочное количество элементов!")
            continue
        # проверка 2
        prov2 = ""
        for i in A_str:
            prov2 += i
        prov2 = prov2.replace("-", "")
        if not prov2.isdigit():
            print("В списке должны быть только цифры!")
            continue

        out_A = []
        for i in A_str:
            if int(i) < 0:
                out_A.append("("+i+")")
            else:
                out_A.append(i)
        # делаем матрицу int
        A=[]
        for i in A_str:
            A.append(int(i))
        opred_A = opred_3x3(A)
        print(opred_3x3_sol(A))
        print()
        return A, opred_A, out_A
def choice3():
    while True:
        # --------ЭТАП1--------
        print("\n1)Посчитаем определитель")
        A, opred_A, out_A = choice2_2()
        # --------ЭТАП2--------
        print("2)Равен ли определитель 0?")
        if opred_A != 0:
            print(opred_A, "≠ 0  Это значит что всё хорошо\n")
        else:
            input("Да, определитель твоей матрицы равен 0.\nВроде как это значит что обратной матрицы не существует..\nНа этом мои полномочия всё.")
            return
        # --------ЭТАП3--------
        print("3)Считаем D строки\n")
        outD = []
        for i in A:
            if i < 0:
                outD.append(str(i))
            else:
                outD.append(" "+str(i))
        
        D11 = (A[4]*A[7]-A[5]*A[8])*(-1)**2
        D12 = (A[3]*A[8]-A[5]*A[6])*(-1)**3
        D13 = (A[3]*A[7]-A[4]*A[6])*(-1)**4

        D21 = (A[1]*A[8]-A[2]*A[7])*(-1)**3
        D22 = (A[0]*A[8]-A[2]*A[6])*(-1)**4
        D23 = (A[0]*A[7]-A[1]*A[6])*(-1)**5

        D31 = (A[1]*A[5]-A[2]*A[4])*(-1)**4
        D32 = (A[0]*A[5]-A[2]*A[3])*(-1)**5
        D33 = (A[0]*A[4]-A[1]*A[3])*(-1)**6

        print("D₁₁=(-1)²({} {}) = {}\n         ({} {})".format(outD[4], outD[5], D11, outD[7], outD[8]))
        print("D₁₂=(-1)³({} {}) = {}\n         ({} {})".format(outD[3], outD[5], D12, outD[6], outD[8]))
        print("D₁₃=(-1)⁴({} {}) = {}\n         ({} {})\n".format(outD[3], outD[4], D13, outD[6], outD[7]))
        
        print("D₂₁=(-1)³({} {}) = {}\n         ({} {})".format(outD[1], outD[2], D21, outD[7], outD[8]))
        print("D₂₂=(-1)⁴({} {}) = {}\n         ({} {})".format(outD[0], outD[2], D22, outD[6], outD[8]))
        print("D₂₃=(-1)⁵({} {}) = {}\n         ({} {})\n".format(outD[0], outD[1], D23, outD[6], outD[7]))

        print("D₃₁=(-1)⁴({} {}) = {}\n         ({} {})".format(outD[1], outD[2], D31, outD[4], outD[5]))
        print("D₃₂=(-1)⁵({} {}) = {}\n         ({} {})".format(outD[0], outD[2], D32, outD[3], outD[5]))
        print("D₃₃=(-1)⁶({} {}) = {}\n         ({} {})\n".format(outD[0], outD[1], D33, outD[3], outD[4]))
       
        # --------ЭТАП4--------
        print("4)Вставляем D элементы в матрицу\n")
        Dmat = []
        Dmat.append(D11)
        Dmat.append(D12)
        Dmat.append(D13)
        Dmat.append(D21)
        Dmat.append(D22)
        Dmat.append(D23)
        Dmat.append(D31)
        Dmat.append(D32)
        Dmat.append(D33)

        out = []
        for i in Dmat:
            if len(str(i)) == 1:
                out.append("   "+str(i))
            elif len(str(i)) == 2:
                out.append("  "+str(i))
            elif len(str(i)) == 3:
                out.append(" "+str(i))
            else:
                out.append(str(i))    
        print("({} {} {})\n|{} {} {}|\n({} {} {})\n".format(out[0], out[1], out[2], out[3], out[4], out[5], out[6], out[7], out[8]))

        # --------ЭТАП5--------
        print("5)Трансформируем полученную матрицу")
        At = []
        At.append(Dmat[0])
        At.append(Dmat[3])
        At.append(Dmat[6])
        At.append(Dmat[1])
        At.append(Dmat[4])
        At.append(Dmat[7])
        At.append(Dmat[2])
        At.append(Dmat[5])
        At.append(Dmat[8])

        output = []
        for i in At:
            if len(str(i)) == 1:
                output.append("   "+str(i))
            elif len(str(i)) == 2:
                output.append("  "+str(i))
            elif len(str(i)) == 3:
                output.append(" "+str(i))
            else:
                output.append(str(i))    
        print("     ({} {} {})\nAᵗ = ({} {} {})\n     ({} {} {})\n".format(output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7], output[8]))
        # --------ЭТАП6--------
        print("6)Находим обратную матрицу")
        print("A⁻¹ = 1/|A|")
        print(" "*(9+len(str(opred_A)))+"({} {} {})\n".format(output[0], output[1], output[2])+"A⁻¹ = 1/{}*|{} {} {}|\n".format(opred_A,output[3], output[4], output[5])+" "*(9+len(str(opred_A)))+"({} {} {})\n".format(output[6], output[7], output[8]))
        print("     ({}/{} {}/{} {}/{})\nAᵗ = ({}/{} {}/{} {}/{})\n     ({}/{} {}/{} {}/{})\n".format(output[0], opred_A, output[1], opred_A, output[2], opred_A, output[3], opred_A, output[4], opred_A, output[5], opred_A, output[6], opred_A, output[7], opred_A, output[8], opred_A))
        print("Ответ ↑\n")
        print("Здесь можно матрицу выше прогнать через программу \"Photomath\" и упростить её\n")

        # ------ЭТАП1(Проверка)--------
        print("1)ПРОВЕРКА")
        print("A*A⁻¹ = E")
        # сделаем чтобы отрицательные числа в скобочки заключались
        out_At = []
        for i in At:
            if int(i) < 0:
                out_At.append("("+str(i)+")")
            else:
                out_At.append(str(i))
        print("Каждая строка - элемент еденичной матрицы")
        print("{}*{}+{}*{}+{}*{} / {}".format(out_At[0], out_A[0], out_At[3], out_A[1], out_At[6], out_A[2], opred_A))
        print("{}*{}+{}*{}+{}*{} / {}".format(out_At[1], out_A[0], out_At[4], out_A[1], out_At[7], out_A[2], opred_A))
        print("{}*{}+{}*{}+{}*{} / {}\n".format(out_At[2], out_A[0], out_At[5], out_A[1], out_At[8], out_A[2], opred_A))

        print("{}*{}+{}*{}+{}*{} / {}".format(out_At[0], out_A[3], out_At[3], out_A[4], out_At[6], out_A[5], opred_A))
        print("{}*{}+{}*{}+{}*{} / {}".format(out_At[1], out_A[3], out_At[4], out_A[4], out_At[7], out_A[5], opred_A))
        print("{}*{}+{}*{}+{}*{} / {}\n".format(out_At[2], out_A[3], out_At[5], out_A[4], out_At[8], out_A[5], opred_A))

        print("{}*{}+{}*{}+{}*{} / {}".format(out_At[0], out_A[6], out_At[3], out_A[7], out_At[6], out_A[8], opred_A))
        print("{}*{}+{}*{}+{}*{} / {}".format(out_At[1], out_A[6], out_At[4], out_A[7], out_At[7], out_A[8], opred_A))
        print("{}*{}+{}*{}+{}*{} / {}\n".format(out_At[2], out_A[6], out_At[5], out_A[7], out_At[8], out_A[8], opred_A))
        # ------ЭТАП2(Проверка)--------
        print("2)ПРОВЕРКА")
        print("Каждая строка - элемент еденичной матрицы\n")
        # промежутки

        print("{}+{}+{} / {}".format(At[0]*A[0], At[3]*A[1], At[6]*A[2], opred_A))
        print("{}+{}+{} / {}".format(At[1]*A[0], At[4]*A[1], At[7]*A[2], opred_A))
        print("{}+{}+{} / {}\n".format(At[2]*A[0], At[5]*A[1], At[8]*A[2], opred_A))

        print("{}+{}+{} / {}".format(At[0]*A[3], At[3]*A[4], At[6]*A[5], opred_A))
        print("{}+{}+{} / {}".format(At[1]*A[3], At[4]*A[4], At[7]*A[5], opred_A))
        print("{}+{}+{} / {}\n".format(At[2]*A[3], At[5]*A[4], At[8]*A[5], opred_A))

        print("{}+{}+{} / {}".format(At[0]*A[6], At[3]*A[7], At[6]*A[8], opred_A))
        print("{}+{}+{} / {}".format(At[1]*A[6], At[4]*A[7], At[7]*A[8], opred_A))
        print("{}+{}+{} / {}\n".format(At[2]*A[6], At[5]*A[7], At[8]*A[8], opred_A))
        # ------ЭТАП3(Проверка)--------
        print("3)ПРОВЕРКА")
        print("({}/{} {}/{} {}/{})".format(At[0]*A[0]+At[3]*A[1]+At[6]*A[2], opred_A, At[1]*A[0]+At[4]*A[1]+At[7]*A[2], opred_A, At[2]*A[0]+At[5]*A[1]+At[8]*A[2], opred_A))
        print("({}/{} {}/{} {}/{})".format(At[0]*A[3]+At[3]*A[4]+At[6]*A[5], opred_A, At[1]*A[3]+At[4]*A[4]+At[7]*A[5], opred_A, At[2]*A[3]+At[5]*A[4]+At[8]*A[5], opred_A))
        print("({}/{} {}/{} {}/{})\n".format(At[0]*A[6]+At[3]*A[7]+At[6]*A[8], opred_A, At[1]*A[6]+At[4]*A[7]+At[7]*A[8], opred_A, At[2]*A[6]+At[5]*A[7]+At[8]*A[8], opred_A))
        # ------ЭТАП4(Проверка)--------
        print("4)ПРОВЕРКА")
        print("({} {} {})".format((At[0]*A[0]+At[3]*A[1]+At[6]*A[2])/opred_A, (At[1]*A[0]+At[4]*A[1]+At[7]*A[2])/opred_A, (At[2]*A[0]+At[5]*A[1]+At[8]*A[2])/opred_A))
        print("({} {} {})".format((At[0]*A[3]+At[3]*A[4]+At[6]*A[5])/opred_A, (At[1]*A[3]+At[4]*A[4]+At[7]*A[5])/opred_A, (At[2]*A[3]+At[5]*A[4]+At[8]*A[5])/opred_A))
        print("({} {} {})\n".format((At[0]*A[6]+At[3]*A[7]+At[6]*A[8])/opred_A, (At[1]*A[6]+At[4]*A[7]+At[7]*A[8])/opred_A, (At[2]*A[6]+At[5]*A[7]+At[8]*A[8])/opred_A))

        print(" "*31+"(1 0 0)"+"\n"+"Если эта матрица выглядит так: (0 1 0)\n"+"то всё хорошо"+" "*18+"(0 0 1)\n")
        return
def choice4_1():
    print("\nЭтот блок вычисляет разложение вектора \"а\" в трёхмерном базисе\nv.0.2.0(After Armageddon)")
    base = []

    first = True
    while True:
        # ввод
        if first:
            print("\nВ", end = "")
        else:
            print("\nЕщё раз в", end = "")
        base = input("ведите название всех трёх векторов базиса и их значения подряд через пробелы\nНапример: p 3 -2 4 g -2 1 3 r 7 -4 1\n")
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
        print("!! Над каждой буквой векторов нужно нарисовать стрелочку !!")

        print("\nВы ввели:")
        print("{} = ({}; {}; {})".format(base[0], base[1], base[2], base[3]))
        print("{} = ({}; {}; {})".format(base[4], base[5], base[6], base[7]))
        print("{} = ({}; {}; {})".format(base[8], base[9], base[10], base[11]))
        print("{} = ({}; {}; {})\n".format(a[0], a[1], a[2], a[3]))
        
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

        #-------------------------------------------создание всех дельта матриц-------------------------------------------
        # треугольник-----------------------
        mtx_int = []
        j = [1, 5, 9, 2, 6, 10, 3, 7, 11]       # mtx_int
        for i in j:
            mtx_int.append(int(base[i]))
        # выравнивание пробелами
        mtx = []
        for i in mtx_int:
            if len(str(i)) == 1:
                mtx.append("  "+str(i))               # mtx
            elif len(str(i)) == 2:
                mtx.append(" "+str(i))
            else:
                mtx.append(str(i))
        # переделываем все строчные элементы а в цифоровые
        b = list(a)
        a = []
        for i in b[1:]:
            a.append(int(i))
        # a с пробелами
        a_str = []
        for i in a:
            if len(str(i)) == 1:
                a_str.append("  "+str(i))
            elif len(str(i)) == 2:                    # a_str
                a_str.append(" "+str(i))
            else:
                a_str.append(i)
        # треугольник1----------------------
        mtx1_int = list(mtx_int)
        mtx1_int[0] = a[0]
        mtx1_int[3] = a[1]
        mtx1_int[6] = a[2]
        # выравнивание пробелами
        mtx1 = list(mtx)
        mtx1[0] = a_str[0]
        mtx1[3] = a_str[1]
        mtx1[6] = a_str[2]
        # треугольник2----------------------
        mtx2_int = list(mtx_int)
        mtx2_int[1] = a[0]
        mtx2_int[4] = a[1]
        mtx2_int[7] = a[2]
        # выравнивание пробелами
        mtx2 = list(mtx)
        mtx2[1] = a_str[0]
        mtx2[4] = a_str[1]
        mtx2[7] = a_str[2]
        # треугольник3----------------------
        mtx3_int = list(mtx_int)
        mtx3_int[2] = a[0]
        mtx3_int[5] = a[1]
        mtx3_int[8] = a[2]
        # выравнивание пробелами
        mtx3 = list(mtx)
        mtx3[2] = a_str[0]
        mtx3[5] = a_str[1]
        mtx3[8] = a_str[2]
        # вывод всего------------------------------------------------------------
        # треугольник
        print(" |{};{};{}|\nΔ|{};{};{}|\n |{};{};{}| = ".format(mtx[0], mtx[1], mtx[2], mtx[3], mtx[4], mtx[5], mtx[6], mtx[7], mtx[8]), end = "")
        opred_mtx = opred_3x3_sol(mtx_int)
        print(opred_mtx,"\n")
        # треугольник1
        print("  |{};{};{}|\nΔ₁|{};{};{}|\n  |{};{};{}| = ".format(mtx1[0], mtx1[1], mtx1[2], mtx1[3], mtx1[4], mtx1[5], mtx1[6], mtx1[7], mtx1[8]), end = "")
        opred_mtx1 = opred_3x3_sol(mtx1_int)
        print(opred_mtx1,"\n")
        # треугольник2
        print("  |{};{};{}|\nΔ₂|{};{};{}|\n  |{};{};{}| = ".format(mtx2[0], mtx2[1], mtx2[2], mtx2[3], mtx2[4], mtx2[5], mtx2[6], mtx2[7], mtx2[8]), end = "")
        opred_mtx2 = opred_3x3_sol(mtx2_int)
        print(opred_mtx2,"\n")
        # треугольник3
        print("  |{};{};{}|\nΔ₃|{};{};{}|\n  |{};{};{}| = ".format(mtx3[0], mtx3[1], mtx3[2], mtx3[3], mtx3[4], mtx3[5], mtx3[6], mtx3[7], mtx3[8]), end = "")
        opred_mtx3 = opred_3x3_sol(mtx3_int)
        print(opred_mtx3,"\n")

        # ---------------Этап3--------------------------
        print("Этап3\nАльфы")
        alf1 = opred_3x3(mtx1_int)/opred_3x3(mtx_int)
        alf2 = opred_3x3(mtx2_int)/opred_3x3(mtx_int)
        alf3 = opred_3x3(mtx3_int)/opred_3x3(mtx_int)
        print("λ₁ = {}/{} = {}".format(opred_3x3(mtx1_int), opred_3x3(mtx_int), alf1))
        print("λ₂ = {}/{} = {}".format(opred_3x3(mtx2_int), opred_3x3(mtx_int), alf2))
        print("λ₃ = {}/{} = {}\n".format(opred_3x3(mtx3_int), opred_3x3(mtx_int), alf3))
        print("Ответ:")

        # преобразования
        if str(alf1).split(".")[1] == "0":
            alf1 = round(alf1)
        if str(alf2).split(".")[1] == "0":
            alf2 = round(alf2)
        if str(alf3).split(".")[1] == "0":
            alf3 = round(alf3)

        k = [alf2, alf3]
        l = []
        for i in k:
            # чтобы 1 исчезали
            if i == "1":
                j = ""
            elif i == "-1":
                j = "-"
            else:
                j = str(i)
            # чтобы у положительных был "+"
            if i > 0:
                l.append("+"+j)
            else:
                l.append(j)

        print("{} = {}{}{}{}{}{}".format(b[0], alf1, base[0], l[0], base[4], l[1], base[8]))
        return
def choice4_2():
    print("\nЭтот блок вычисляет разложение вектора \"а\" в двухмерном базисе\nv.0.1.0")
    base = []
    first = True
    while True:
        # ввод
        if first:
            print("\nВ", end = "")
        else:
            print("\nЕщё раз в", end = "")
        base = input("ведите название двух векторов базиса и их значения подряд через пробелы\nНапример: p 3 -2 g -2 1\n")
        base = base.split()
        print()
        
        
        # проверка базиса
        if len(base) != 6:
            print("Неверное количество символов!")
            first = False
            continue
        
        # ввод разлагаемого вектора
        first = True
        while True:
            if first:
                print("По аналогии ", end = "")
            else:
                print("Ещё раз ", end = "")
            a = input("введите данные разлагаемого вектора\nНапример: a 25 -15\n") 
            a = a.split()
            
            # проверка разлагаемого вектора
            if len(a) != 3:
                print("Неверное количество символов!")
                first = False
            else:
                break
        # ---------------------Дано---------------------
        print("!! Над каждой буквой векторов нужно нарисовать стрелочку !!")

        print("\nВы ввели:")
        print("{} = ({}; {})".format(base[0], base[1], base[2]))
        print("{} = ({}; {})".format(base[3], base[4], base[5]))
        print("{} = ({}; {})\n".format(a[0], a[1], a[2]))
        
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
        print("\nЭтап1")
        
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
        print("{}λ₁{}λ₂ = {}".format(base[1], base_out1[4], a[1]))
        print("{}λ₁{}λ₂ = {}\n".format(base[2], base_out1[5], a[2]))

        # ---------------Этап2--------------------------
        print("Этап2\nТреугольнички дельточки")

        #-------------------------------------------создание всех дельта матриц-------------------------------------------
        # треугольник-----------------------
        mtx_int = []
        j = [1, 4, 2, 5]       # mtx_int
        for i in j:
            mtx_int.append(int(base[i]))
        # выравнивание пробелами
        mtx = []
        for i in mtx_int:
            if len(str(i)) == 1:
                mtx.append("  "+str(i))               # mtx
            elif len(str(i)) == 2:
                mtx.append(" "+str(i))
            else:
                mtx.append(str(i))
        # переделываем все строчные элементы а в цифоровые
        b = list(a)
        a = []
        for i in b[1:]:
            a.append(int(i))
        # a с пробелами
        a_str = []
        for i in a:
            if len(str(i)) == 1:
                a_str.append("  "+str(i))
            elif len(str(i)) == 2:                    # a_str
                a_str.append(" "+str(i))
            else:
                a_str.append(i)
        # треугольник1----------------------
        mtx1_int = list(mtx_int)
        mtx1_int[0] = a[0]
        mtx1_int[2] = a[1]
        # выравнивание пробелами
        mtx1 = list(mtx)
        mtx1[0] = a_str[0]
        mtx1[2] = a_str[1]
        # треугольник2----------------------
        mtx2_int = list(mtx_int)
        mtx2_int[1] = a[0]
        mtx2_int[3] = a[1]
        # выравнивание пробелами
        mtx2 = list(mtx)
        mtx2[1] = a_str[0]
        mtx2[3] = a_str[1]
        # вывод всего------------------------------------------------------------
        # треугольник
        print(" |{};{}|\nΔ|{};{}| = ".format(mtx[0], mtx[1], mtx[2], mtx[3]), end = "")
        opred_mtx = opred_2x2_sol(mtx_int)
        print(opred_mtx,"\n")
        # треугольник1
        print("  |{};{}|\nΔ₁|{};{}| = ".format(mtx1[0], mtx1[1], mtx1[2], mtx1[3]), end = "")
        opred_mtx1 = opred_2x2_sol(mtx1_int)
        print(opred_mtx1,"\n")
        # треугольник2
        print("  |{};{}|\nΔ₂|{};{}| = ".format(mtx2[0], mtx2[1], mtx2[2], mtx2[3]), end = "")
        opred_mtx2 = opred_2x2_sol(mtx2_int)
        print(opred_mtx2,"\n")

        # ---------------Этап3--------------------------
        print("Этап3\nАльфы")
        alf1 = opred_2x2(mtx1_int)/opred_2x2(mtx_int)
        alf2 = opred_2x2(mtx2_int)/opred_2x2(mtx_int)
        # преобразования
        if str(alf1).split(".")[1] == "0":
            alf1 = round(alf1)
        if str(alf2).split(".")[1] == "0":
            alf2 = round(alf2)

        print("λ₁ = {}/{} = {}".format(opred_2x2(mtx1_int), opred_2x2(mtx_int), alf1))
        print("λ₂ = {}/{} = {}\n".format(opred_2x2(mtx2_int), opred_2x2(mtx_int), alf2))
        print("Ответ:")
        # чтобы 1 исчезали
        if str(alf2) == "1":
            j = ""
        elif str(alf2) == "-1":
            j = "-"
        else:
            j = str(alf2)
        # чтобы у положительных был "+"
        if alf2 > 0:
            alf2 = ("+"+j)
        else:
            alf2 = j

        print("{} = {}{}{}{}".format(b[0], alf1, base[0], alf2, base[4]))
        return
def choice5_1():
    print("\nЭтот блок находит ВЕКТОРНОЕ произведение двух трёхмерных векторов\nv.0.1.1(PC)")
    first = True
    while True:
        vec = []
        # ввод
        if first:
            print("\nВ", end = "")
        else:
            print("\nЕщё раз в", end = "")
        vec = input("ведите название двух векторов и их значения подряд через пробелы\nНапример: a -1 0 -3 b 4 -3 2\n")
        vec = vec.split()
        print()
        # проверка
        if len(vec) != 8:
            print("Неверное количество символов!")
            first = False
            continue
        # Всё в матрицу
        mtx_str = ["i", "j", "k", vec[1], vec[2], vec[3], vec[5], vec[6], vec[7]]
        # выравнивание пробелами
        mtxout_str = []
        for i in mtx_str:
            if len(i) == 1:
                mtxout_str.append("  "+i)
            elif len(i) == 2:
                mtxout_str.append(" "+i)
            else:
                mtxout_str.append(i)
        print("!! Над каждой буквой векторов, а также над i, j, k нужно нарисовать стрелочку !!\n")
        print(" "*(len(vec[0])+len(vec[4])+4)+"|{};{};{}|".format(mtxout_str[0], mtxout_str[1], mtxout_str[2]))
        print("{}×{} = |{};{};{}| = ".format(vec[0], vec[4], mtxout_str[3], mtxout_str[4], mtxout_str[5]))
        print(" "*(len(vec[0])+len(vec[4])+4)+"|{};{};{}|".format(mtxout_str[6], mtxout_str[7], mtxout_str[8]))
        
        # Промежуточные штуки
        el = [int(vec[2])*int(vec[7]), int(vec[3])*int(vec[6]), int(vec[1])*int(vec[7]), int(vec[3])*int(vec[5]), int(vec[1])*int(vec[6]), int(vec[2])*int(vec[5])]

        print("\n= i|{};{}| - j|{};{}| + k|{};{}| =".format(mtxout_str[4], mtxout_str[5], mtxout_str[3], mtxout_str[5], mtxout_str[3], mtxout_str[4]))
        print("   |{};{}|    |{};{}|    |{};{}|".format(mtxout_str[7], mtxout_str[8], mtxout_str[6], mtxout_str[8], mtxout_str[6], mtxout_str[7]))

        # Промежуточные штуки
        el = [int(vec[2])*int(vec[7]), int(vec[3])*int(vec[6]), int(vec[1])*int(vec[7]), int(vec[3])*int(vec[5]), int(vec[1])*int(vec[6]), int(vec[2])*int(vec[5])]
        el2 = [el[0]-el[1], el[2]-el[3], el[4]-el[5]]
        print("\n= i({}-{}) - j({}-{}) + k({}-{}) = {}i - {}j + {}k (Разложение по орто-норм. базису)".format(el[0], el[1], el[2], el[3], el[4], el[5], el2[0], el2[1], el2[2]))
        print("Ответ: {}×{} = ({};{};{})\n".format(vec[0], vec[4], el2[0], el2[1], el2[2]))
        return
def choice5_2():
    print("\nЭтот блок находит СКАЛЯРНОЕ произведение двух трёхмерных векторов\nv.0.1.0")
    first = True
    while True:
        vec = []
        # ввод
        if first:
            print("\nВ", end = "")
        else:
            print("\nЕщё раз в", end = "")
        vec = input("ведите название двух векторов и их значения подряд через пробелы\nНапример: a -1 0 -3 b 4 -3 2\n")
        vec = vec.split()
        print()
        # проверка
        if len(vec) != 8:
            print("Неверное количество символов!")
            first = False
            continue
        list_int = [int(vec[1]), int(vec[2]), int(vec[3]), int(vec[5]), int(vec[6]), int(vec[7])]

        # Промежуточные штуки
        el_int = [list_int[0]*list_int[3], list_int[1]*list_int[4], list_int[2]*list_int[5]]
        sol = list_int[0]*list_int[3] + list_int[1]*list_int[4] + list_int[2]*list_int[5]

        # сделаем чтобы отрицательные числа в скобочки заключались
        list_str = []
        el_str = []
        for i in list_int:
            if i < 0:
                list_str.append("("+str(i)+")")
            else:
                list_str.append(i)
        for i in el_int:
            if i < 0:
                el_str.append("("+str(i)+")")
            else:
                el_str.append(i)

        print("({}⃗,{}⃗) = {}*{} + {}*{} + {}*{} = {}+{}+{} = {}\n".format(vec[0], vec[4], list_str[0], list_str[3], list_str[1], list_str[4], list_str[2], list_str[5], el_str[0], el_str[1], el_str[2], sol))
        return
def choice5_3():
    print("\nЭтот блок вычисляет cмешанное произведение трёх векторов\nv.0.2.1")
    while True:
        vec = []
        # ввод первого вектора
        while True:
            a = input("\nВведите название и значения ПЕРВОГО вектора через пробелы\nНапример: a -1 0 -3\n")
            a = a.split()
            if len(vec) != 4:
                print("Неверное количество символов!")
                continue
            else:
                break
        vec.append(a)
        # ввод второго вектора
        while True:
            a = input("\nВведите название и значения ВТОРОГО вектора через пробелы\nНапример: b 4 -3 2\n")
            a = a.split()
            if len(vec) != 4:
                print("Неверное количество символов!")
                continue
            else:
                break
        vec.append(a)
        # ввод третьего вектора
        while True:
            a = input("\nВведите название и значения ТРЕТЬЕГО вектора через пробелы\nНапример: c 0 -1 0\n")
            a = a.split()
            if len(vec) != 4:
                print("Неверное количество символов!")
                continue
            else:
                break
        vec.append(a)

        # проверка всего
        if len(vec) != 12:
            print("Ошибка! Неверное количество символов в трёх векторах в сумме!")
            continue
        # Всё в матрицу
        list_int = [int(vec[1]), int(vec[2]), int(vec[3]), int(vec[5]), int(vec[6]), int(vec[7]), int(vec[9]), int(vec[10]), int(vec[11])]
        
        print("!! Над каждой буквой векторов нужно нарисовать стрелочку !!\n")
        print(" "*(len(vec[0])+len(vec[4])+len(vec[8])+7)+"|{};{};{}|".format(list_int[0], list_int[1], list_int[2]))
        print("<{},{},{}> = |{};{};{}|".format(vec[0], vec[4], vec[8], list_int[3], list_int[4], list_int[5]))
        print(" "*(len(vec[0])+len(vec[4])+len(vec[8])+7)+"|{};{};{}| = ".format(list_int[6], list_int[7], list_int[8]), end = "")
        print(opred_3x3_sol(list_int))
def choice6():
    print("\nЭтот блок вычисляет длину трёхммерного вектора |a⃗| (получится число)\nv.0.1.0")
    while True:
        # ввод
        vec = input("Введите название вектора и его значения подряд через пробелы\nНапример: a -9 10 3\n")
        vec = vec.split()
        # проверка
        if len(vec) != 4:
            print("Неверное количество символов!")
            continue

        # Промежуточные штуки
        el = [int(vec[1])**2, int(vec[2])**2, int(vec[3])**2]
        el2 = el[0]+el[1]+el[2]
        sol = el2**0.5
        print("\n|{}⃗| = √({}²+{}²+{}²) = √({}+{}+{}) = √{} = {}\n".format(vec[0], vec[1], vec[2], vec[3], el[0], el[1], el[2], el2, sol))
# Прямые
def choice7():
    print("\nЭтот блок вычисляет точку пересечения двух прямых\nv.0.1.0")
    while True:
        # ввод
        line1 = input("В уравнение вида Ax+By+D=0 описывающую ПЕРВУЮ прямую введите значения коэфициентов A, B, D подряд через пробелы\nНапример: 3 -4 -6\n")
        line1 = line1.split()
        # проверка 1
        if len(line1) != 3:
            print("Неверное количество символов!")
            continue

        # ввод
        line2 = input("В уравнение вида Ax+By+D=0 описывающую ВТОРУЮ пямую введите значения коэфициентов A, B, D подряд через пробелы\nНапример: 2 5 2\n")
        line2 = line2.split()
        # проверка 2
        if len(line1) != 3:
            print("Неверное количество символов!")
            continue

        # преобразования line 1
        line1_out = []
        for i in line1:
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
                    line1_out.append("+"+j)
                else:
                    line1_out.append(j)
            else:
                line1_out.append(i)

        # преобразования line2
        line2_out = []
        for i in line2:
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
                    line2_out.append("+"+j)
                else:
                    line2_out.append(j)
            else:
                line2_out.append(i)

        print("\nВы ввели:")
        print("{"+"{}x{}y{} = 0".format(line1[0], line1_out[1], line1_out[2]))
        print("{"+"{}x{}y{} = 0\n".format(line2[0], line2_out[1], line2_out[2]))

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

        # преобразования 3 -----------------------------------------
        
        # преобразования line 1
        line1_out = []
        for i in line1:
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
                    line1_out.append("+"+j)
                else:
                    line1_out.append(j)
            else:
                line1_out.append(i)
        # преобразования line2
        line2_out = []
        for i in line2:
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
                    line2_out.append("+"+j)
                else:
                    line2_out.append(j)
            else:
                line2_out.append(i)

        if int(line1[2]) < 0:
            line1[2] = line1[2][1:]
            line1_out[2] = line1_out[2][1:]
        else:
            line1[2] = "-"+str(line1[2])
            line1_out[2] = "-"+str(line1_out[2][1:])

        if int(line2[2]) < 0:
            line2[2] = line2[2][1:]
            line2_out[2] = line2_out[2][1:]
        else:
            line2[2] = "-"+str(line2[2])
            line2_out[2] = "-"+str(line2_out[2][1:])

        print("\n{"+"{}x{}y = {}".format(line1[0], line1_out[1], line1_out[2]))
        print("{"+"{}x{}y = {}\n".format(line2[0], line2_out[1], line2_out[2]))

        lines = line1 + line2
        lines_int = []
        for i in lines:
            lines_int.append(int(i))
        outD = []
        for i in lines:
            if int(i) < 0:
                outD.append(i)
            else:
                outD.append(" "+i)
        
        D  = (lines_int[0]*lines_int[4]-lines_int[1]*lines_int[3])
        D1 = (lines_int[1]*lines_int[5]-lines_int[2]*lines_int[4])*-1
        D2 = (lines_int[0]*lines_int[5]-lines_int[2]*lines_int[3])

        print("D  =|{};{}| = {}\n    |{};{}|".format(outD[0], outD[1], D, outD[3], outD[4]))
        print("D₁ =(-1)¹|{};{}| = {}\n         |{};{}|".format(outD[1], outD[2], D1, outD[4], outD[5]))
        print("D₂ =(-1)²|{};{}| = {}\n         |{};{}|".format(outD[0], outD[2], D2, outD[3], outD[5]))
        
        i, j =socrat(D1,D)
        k = D1/D
        if i == D1:
            print("\nx = {}/{} = {}".format(D1,D,k))
        else:
            print("\nx = {}/{} = {}/{} = {}".format(D1,D,i,j,k))

        i, j =socrat(D2,D)
        k = D2/D
        if i == D2:
            print("y = {}/{} = {}".format(D2,D,k))
        else:
            print("y = {}/{} = {}/{} = {}".format(D2,D,i,j,k))

        break
#=====================ПРОГРАММА=====================
run = True
while run:
    # ВЫБОР
    print('by: Тимофей\nПриятного пользования)\n')
    print('Multi - Это сборник из 11 вычислительных программ и 6 скрытых вспомогательных утилит под авторством Тимофея\n\nВыберите что вы хотите сделать?')
    choice = input('''1)Перевести число из одной системы счисления в другую
2)Найти определитель матрицы методом треугольников (2x2 или 3x3)
3)Вычислить обратную матрицу
4)Разложение вектора (в двухмерном или трёхмерном базисе)
5)Произведение векторов
6)Найти длину вектора |a⃗| (число)

Прямые
7)Найти точку пересечения двух прямых
(1-7) ''')

    if choice == "1":
        choice1()
    elif choice == '2':
    # Подвыбор
        choice = input("\n1)2x2\n2)3x3\n")
        if choice == "1":
            choice2_1()
        elif choice == "2":
            choice2_2()
        elif choice != '1' or choice != '2':
            print("Некорректный ввод!")
    elif choice == '3':
        choice3()
    elif choice == '4':
    # Подвыбор
        choice = input("\n1)Трёхмерный базис\n2)Двухмерный базис\n")
        if choice == "1":
            choice4_1()
        elif choice == "2":
            choice4_2()
        elif choice != '1' and choice != '2':
            print("Некорректный ввод!")
    elif choice == '5':
    # Подвыбор
        choice = input("\n1)Векторное произведение a⃗×b⃗ или [a⃗,b⃗] (3 координаты)\n2)Скалярное произведение a⃗·b⃗ или (a⃗,b⃗) (число)\n3)Смешанное произведение a⃗ b⃗ c⃗ или <a⃗, b⃗, c⃗>\n")
        if choice == "1":
            choice5_1()
        elif choice == "2":
            choice5_2()
        elif choice == "3":
            choice5_3()
        elif choice != '1' or choice != '2':
            print("Некорректный ввод!")
    elif choice == '6':
        choice6()
    elif choice == '7':
        choice7()
    #elif choice != '1' or choice != '2' or choice != '3' or choice != '4' or choice != '5':
    else:
        print("Некорректный ввод!")

    # ----------------------------------------------------------------------------------------
    ex = input("Удивительный факт: в этой программе ровно 1107 строк!\n1)Продолжить\n2)Выход\n")
    if ex == "2":
        run = False
    elif ex == '1':
        pass
    # else реагирует на break в функциях
    #elif ex != '1' and ex != '2':
    else:
        print("Некорректный ввод!")