print("/ НАЖМИ ЛЮБУЮ КЛАВИШУ /")
vhod = input()
print("/ ДАННАЯ ПРОГРАММА ВЫЧИСЛЯЕТ СРЕДНИЙ БАЛЛ ДИПЛОМА /")
print("/ ЗАГРУЗИТЬ ГОТОВЫЕ ДИСЦИПЛИНЫ НА МОМЕНТ 5-ГО СЕМЕСТРА/")
print("/ или /")
print("/ НАЧАТЬ ЗАПИСЬ ДИСЦИПЛИН С НУЛЯ /")
print("/ [1/0] /")
choose = int(input())
arr_for_values = []
alpathet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ъ','ы','э','ю','я','.','Й','Ц','У','К','Е','Н','Г','Ш','Щ','З','Х','Ф','В','А','П','Р','О','Л','Д','Ж','Э','Я','Ч','С','М','И','Т','Б','Ю'' ',]

# def check_alth(i):
#     k = 0
#     for k in range(len(alpathet)):
#         if i != alpathet[k]:
#             print("err: bad input #" + alpathet[k])
#         i = input()   
#         k = k + 1
    

various = input()
check_alth(various)
if choose == 1 : 

    ready_disciplines = {'Иностранный язык':None,'Военная история': None,'История':None,'Философия':None,'Психология':None,'Экономика':None,'Социология':None, 'Мат.Анализ':None,'АГиЛА':None,'СГМА':None,'СГА':None,'ТВМ':None,'Информатика':None,'Физика':None,'ДСМ':None,'ЯП':None,'ОС':None,'РХБЗ':None,'Топография':None,'БЖД':None,'АП':None,'Инж.Подготовка':None,'Методы Программирования':None,'СМАД':None,'КС':None}

    _len = len(ready_disciplines)
    sum = 0
    i = 0
    for key in ready_disciplines:
        
        number = int(input(key + ': '))
        if number != 3 and number != 4 and number != 5:
            print("Ты долбаеб!")
            ready_disciplines[key] = int(input(key + ': '))
        else:
            ready_disciplines[key] = number
        sum += ready_disciplines[key]
        i = i + 1
        j = i
    print("Это все ? [1/0]:")
    decision = int(input())
    if decision == 1:
        print("Количество дисциплин на вводе: " + str(j))
        print("Общая сумма баллов: " + str(sum))
        print("Cредний балл: " + str(sum/_len))
    elif decision ==  0:
        print("Количество новых дисциплин:")
        x = int(input())
        new_disc = []
        for k in range(x):
            new_disc.append(str(input())) 
        print("Введите оценки по новым дисциплинам:")
        for k in range(x):
            print(new_disc[k])
            arr_for_values.append(int(input()))
        s4et4ik = k + 1
        sum2 = 0
        for k in range(x):
            sum2 = sum2 + arr_for_values[k]
        print("Новая общая сумма баллов: " + str(sum2))
        print("Новое количество дисциплин на вводе: " + str(s4et4ik))
        print("Посчитать среднее ОБЩЕЕ\ЧАСТНОЕ [1/0]")
        rewenie = int(input())
        if rewenie == 0 :
            print("other middle value :" + str(sum2/s4et4ik))
        elif rewenie == 1 :
            mid_sum = sum + sum2
            mid_len = j + s4et4ik
            print("Main_sum : " + str(mid_sum))
            print("Main number of disc : " + str(mid_len))
            print("Main Mid :" + str(mid_sum/mid_len)) 
    print("___________________________________________________________\n")
    print(" Print raport? [1/0] ")
    raport = int(input())
    if raport == 0 :
        print("PROGPAMM IS DONE !")
    elif raport == 1 : 
        ouf = open("C:/Users/Dmitry/Desktop/raport", 'w')
        x1 = len(list(ready_disciplines)) - 1
        space = " - "
        space2 = "\n"
        for i in ready_disciplines :
        # !!!блять заебалa какого хуя эта строка не работает    
            ouf.write(list(ready_disciplines)[i] + space + space2)
elif choose == 0 :
    
    print("Number of new disc:")
    x = int(input())
    new_disc = []
    for k in range(x):
        new_disc.append(str(input()))
        
    print("Input new marks of disc:")
    arr_for_values = []
    for k in range(x):
        print(new_disc[k])
        arr_for_values.append(int(input()))
    s4et4ik = k + 1
    sum2 = 0
    for k in range(x):
        sum2 = sum2 + arr_for_values[k]
    print("Новая общая сумма баллов: " + str(sum2))
    print("Новое количество дисциплин на вводе: " + str(s4et4ik))
    print("Средний балл: " + str(sum2/s4et4ik))
    print("_____________________________________________")
    print("СОСТАВИТЬ ОТЧЕТ [1/0]")
    raport = int(input())
    if raport == 0 :
        print("PROGRAMM IS DONE !")
    elif raport == 1 :
        ouf = open('C:/Users/Dmitry/Desktop/raport.txt','w')
        r = 0
        space = " - "
        space2 = "\n"
        for i in new_disc :
            ouf.write(i + space + str(arr_for_values[r]))
            ouf.write("\n")
            r = r + 1
        ouf.write("_________________________________________\n")
        ouf.write("Новая общая сумма баллов: " + str(sum2)+ space2)
        ouf.write("Новое количество дисциплин на вводе: " + str(s4et4ik)+ space2)
        ouf.write("Средний балл: " + str(sum2/s4et4ik) + space2)
        
        
    

    



    



    
    



