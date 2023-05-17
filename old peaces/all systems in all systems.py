#Это штука, которая всё здесь считает и выводит резульат 
def convert(chislo,number_system,target_system): 
    #chislo(str); number_system(int);target_system(int) 
    i10 = int(str(chislo),number_system) 
    alfabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    result="" 
    while i10>0: 
        k = i10%target_system   #очередная цифра 
        result = alfabet[k]+result #приклеиваем спереди в соответствии с алфавитом 
        i10 = i10//target_system 
    return result 
#------------------------------------------------------------------- 
#А здесь основная логика программы 
quite_or_not = "y" 
default_or_not = 0 
while True: 
    if quite_or_not == "y" or quite_or_not == "Y": 
         
        x = input("Введите число\n") 
        y = int(input("В какой системе это число? (от 2 до 37)\n")) 
        if y >= 37: 
            print("\nТы щас серьёзно? 37?? Я ясно написал \"ДО 37\"\n")  #просто пасхалочка 
            break 
 
 
        if not default_or_not:       #вопросы о выборе 
            default_or_not = int(input("Перевести в системы (2-16), или хотите ввести собственный список систем от 2 до 37?\n(1/2) ")) 
            if not(0<default_or_not<3): 
                print("Число не соответстует интервалу. Либо 1 либо 2.") 
                default_or_not = 0 
        else: 
            default_or_not = int(input("2-16; ввести свои системы; предыдущий список систем\n(1/2/3) ")) 
 
                    #результат от выбора 
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
        quit() 
    elif quite_or_not == "у":  #просто пасхалочка 
        print("Если что, \"y\" и \"n\" это yes или no\nА ты, как я вижу, забил на языки и написал русскую \"у\"?\nБоже.. чел..") 
    else: 
        print("\nНадо ввести \"y\" (yes) или \"n\" (no)") 
     
    quite_or_not = input("Ещё раз? (y/n)") 
 
s = input("Нажмите любую клавишу для выхода\n")