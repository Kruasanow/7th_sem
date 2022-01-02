print('-------------------------------------------------------------------')
print('----Программы выполнения операций над 2х \ 10х \ 16х числами-------')
print('-------------------------------------------------------------------')
print('-----------------------Выберите операцию---------------------------')
print('-------------------[1-addition \ 2-transition]---------------------')
print('------------------[3-multiplicate \ 4-division]--------------------')
print('-------------------------------------------------------------------')
a = int(input())
if a == 1:
    #----------------------------------------------------------------------#

    print("SYS: Какую систему исчисления использовать [2x or 10x or 16x]", end='- ')
    sistema_4isel=int(input())    
    print("REM: при вводе переменных убедитесь что первая переменная больше второй")
    print("REM: при вводе 16х переменных используйте верхний регистр") 
    print("SYS: Укажите первую переменную ", end='- ')
    first_variable=str(input())    
    print("SYS: Укажите вторую переменную ", end='- ')
    second_variable=str(input())

    #----------------------------------------------------------------------#

    len_of_1st_variable=len(first_variable)
    len_of_2nd_variable=len(second_variable)

    #----------------------------------------------------------------------#

    def Switch_to_decimal(first_variable, len_of_1st_variable):
        first_variable=list(first_variable)
        for i in range(len_of_1st_variable):  
            if first_variable[i]=='A':
                first_variable[i]='10'
            elif first_variable[i]=='B':
                first_variable[i]='11'
            elif first_variable[i]=='C': 
                first_variable[i]='12'
            elif first_variable[i]=='D':
                first_variable[i]='13'
            elif first_variable[i]=='E':
                first_variable[i]='14'
            elif first_variable[i]=='F':
                first_variable[i]='15'
        return first_variable

    #----------------------------------------------------------------------#

    def Switch_to_int (first_variable, len_of_1st_variable):           
        for i in range(len_of_1st_variable):
            first_variable[i]=int(first_variable[i])

    #----------------------------------------------------------------------#

    def Equiv_size (stindex,exit_tool):        
        for i in range(exit_tool):
            stindex.append(0)

    #----------------------------------------------------------------------#

    first_variable=Switch_to_decimal(first_variable, len_of_1st_variable)
    second_variable=Switch_to_decimal(second_variable, len_of_2nd_variable)

    Switch_to_int(first_variable, len_of_1st_variable)
    Switch_to_int(second_variable, len_of_2nd_variable)

    first_variable.reverse()
    second_variable.reverse()

    #----------------------------------------------------------------------#

    if len_of_1st_variable > len_of_2nd_variable:                     
        Equiv_size(second_variable, len_of_1st_variable-len_of_2nd_variable)
    elif len_of_1st_variable < len_of_2nd_variable:
        Equiv_size(first_variable, len_of_2nd_variable-len_of_1st_variable)

    #----------------------------------------------------------------------#

    index1=0
    index2=0
    array=[]
    for i in range(0, max(len_of_1st_variable, len_of_2nd_variable)):       
        index2=first_variable[i]+second_variable[i]+index1
        index1=index2//sistema_4isel
        array.append(index2%sistema_4isel)
    array.append(index2//sistema_4isel)
    array.reverse()

    #----------------------------------------------------------------------#
    # arr -> int

    print('SYS: Результат сложения', end=' - ')
    for i in range(len(array)):            
        if i==0 and array[i]==0:
            continue
        if array[i]==10:
            array[i]='A'
        elif array[i]==11:
            array[i]='B'
        elif array[i]==12: 
            array[i]='C'
        elif array[i]==13:
            array[i]='D'
        elif array[i]==14:
            array[i]='E'
        elif array[i]==15:
            array[i]='F'
        print(array[i], end='')

    exit_tool=input(" ||  SYS: Программа завершена, нажмите любую кнопку")
elif a == 2:
    print("REM: при вводе переменных убедитесь что первая переменная больше второй")
    first_variable=str(input("SYS: Укажите первую переменную - ")) 
    second_variable=str(input("SYS: Укажите вторую переменную - "))

    #----------------------------------------------------------------------#

    len_of_1st_variable=len(first_variable)
    len_of_2nd_variable=len(second_variable)

    #----------------------------------------------------------------------#

    def Switch_to_decimal(first_variable, len_of_1st_variable):
        first_variable=list(first_variable)
        for i in range(len_of_1st_variable):
            if first_variable[i]=='A':
                first_variable[i]='10'
            elif first_variable[i]=='B':
                first_variable[i]='11'
            elif first_variable[i]=='C': 
                first_variable[i]='12'
            elif first_variable[i]=='D':
                first_variable[i]='13'
            elif first_variable[i]=='E':
                first_variable[i]='14'
            elif first_variable[i]=='F':
                first_variable[i]='15'
        return first_variable

    #----------------------------------------------------------------------#

    def Switch_to_int (first_variable, len_of_1st_variable):
        for i in range(len_of_1st_variable):
            first_variable[i]=int(first_variable[i])

    #----------------------------------------------------------------------#

    def Equiv_size (stindex,exit_tool):
        for i in range(exit_tool):
            stindex.append(0)

    #----------------------------------------------------------------------#

    first_variable=Switch_to_decimal(first_variable, len_of_1st_variable)
    second_variable=Switch_to_decimal(second_variable, len_of_2nd_variable)
    Switch_to_int(first_variable, len_of_1st_variable)
    Switch_to_int(second_variable, len_of_2nd_variable)
    first_variable.reverse()
    second_variable.reverse()

    #----------------------------------------------------------------------#

    transition_of_1st_n_sec=len_of_1st_variable-len_of_2nd_variable
    index1=len_of_2nd_variable
    index2=0
    multiplicate1=[0]*(index1+transition_of_1st_n_sec+1)
    multiplicate2=[0]*(transition_of_1st_n_sec+1)
    array=[]
    sistema_4isel=10
    while index2*second_variable[index1-1]<(sistema_4isel//2):
        index2=index2+1
    for i in range(len(multiplicate1)):
        if i!=len(multiplicate1)-1:
            multiplicate1[i]=first_variable[i]
        else: multiplicate1[i]=0
        array.append(multiplicate1[i]*index2)

    #----------------------------------------------------------------------#

    mult_bn_SV_n_ind2=second_variable[index1-1]*index2
    zero=0
    buffer=multiplicate1
    answer=''
    h_index1=''
    h_index2=''
    for i in range(index1, transition_of_1st_n_sec+index1+1):
        zero=min((array[i]*sistema_4isel+array[i-1])//mult_bn_SV_n_ind2, sistema_4isel-1)
        if second_variable[index1-2]*index2*zero>(array[i]*sistema_4isel+array[i-1]-(zero*mult_bn_SV_n_ind2))*sistema_4isel+array[i-2]:
            zero=zero-1
        multiplicate2[i-index1]=zero
    multiplicate2.reverse()
    first_variable.reverse()
    second_variable.reverse()
    for i in multiplicate2:
        answer=answer+str(i)
    answer=int(answer)
    for i in first_variable:
        h_index1=h_index1+str(i)
    for i in second_variable:
        h_index2=h_index2+str(i)
    h_index1=int(h_index1)
    h_index2=int(h_index2)
    remains=h_index1-(answer*h_index2)
    while remains<0:
        answer=answer-1
        remains=h_index1-(answer*h_index2)

    #----------------------------------------------------------------------#

    print('SYS: Результат : ', answer)
    print("SYS: Вывести остаток [y/n] :")
    rem1 = 'y'
    rem2 = 'n'
    O_rem = input()
    if O_rem == rem1:
        print('SYS: Остаток : ', remains)
    elif O_rem == 'n':
        print('SYS: Остаток : ', remains)
    else: print("REM: Выход..")

    #----------------------------------------------------------------------#

    exit_tool=input("SYS: Программы выполнилась, нажмите кнопку для завершения")
elif a == 3:
    print("REM: при вводе переменных убедитесь что первая переменная больше второй")
    print("REM: при вводе 16х переменных используйте верхний регистр") 
    sistema_4isel=int(input("SYS: Какую систему исчисления использовать [2x or 10x or 16x] - ")) 
    first_variable=str(input("SYS: Укажите первую переменную - ")) 
    second_variable=str(input("SYS: Укажите вторую переменную - ")) 

    #----------------------------------------------------------------------#

    len_of_1st_variable=len(first_variable)
    len_of_2nd_variable=len(second_variable)
    zapolnenie_zero=[[0]*(len_of_1st_variable+len_of_2nd_variable) for i in range(len_of_2nd_variable)]

    #----------------------------------------------------------------------#

    def Switch_to_decimal(first_variable, len_of_1st_variable):         
        first_variable=list(first_variable)
        for i in range(len_of_1st_variable):
            if first_variable[i]=='A':
                first_variable[i]='10'
            elif first_variable[i]=='B':
                first_variable[i]='11'
            elif first_variable[i]=='C': 
                first_variable[i]='12'
            elif first_variable[i]=='D':
                first_variable[i]='13'
            elif first_variable[i]=='E':
                first_variable[i]='14'
            elif first_variable[i]=='F':
                first_variable[i]='15'
        return first_variable

    #----------------------------------------------------------------------#

    def Switch_to_int (first_variable, len_of_1st_variable):     
        for i in range(len_of_1st_variable):
            first_variable[i]=int(first_variable[i])

    #----------------------------------------------------------------------#

    def Equiv_size (stindex,exit_tool):    
        for i in range(exit_tool):
            stindex.append(0)

    #----------------------------------------------------------------------#

    first_variable=Switch_to_decimal(first_variable, len_of_1st_variable)
    second_variable=Switch_to_decimal(second_variable, len_of_2nd_variable)

    Switch_to_int(first_variable, len_of_1st_variable)
    Switch_to_int(second_variable, len_of_2nd_variable)

    #----------------------------------------------------------------------#

    if len_of_1st_variable<len_of_2nd_variable:
        array=[]
        zero=0
        zero=len_of_1st_variable
        len_of_1st_variable=len_of_2nd_variable
        len_of_2nd_variable=zero
        array=first_variable
        first_variable=second_variable
        second_variable=array

    #----------------------------------------------------------------------#

    first_variable.reverse()
    second_variable.reverse()

    #----------------------------------------------------------------------#

    Q_index=0
    for i in range(len_of_2nd_variable):  
        for j in range(len_of_1st_variable):
            zapolnenie_zero[i][j+i]=(first_variable[j]*second_variable[i]+Q_index)%sistema_4isel
            Q_index=(first_variable[j]*second_variable[i]+Q_index)//sistema_4isel
        zapolnenie_zero[i][j+i+1]=Q_index
        Q_index=0

    #----------------------------------------------------------------------#

    index1=0
    index2=0
    H_index=0
    S_array=[]
    answer=''
    for j in range(len(zapolnenie_zero[0])):  
        for i in range(len_of_2nd_variable):
            index2=index2+zapolnenie_zero[i][j]
        index2=index2+index1
        index1=index2//sistema_4isel
        S_array.append(index2%sistema_4isel)
        H_index=index2
        index2=0
    if index2//sistema_4isel!=0:
        S_array.append(index2//sistema_4isel)
    S_array.reverse()

    #----------------------------------------------------------------------#

    for i in range(len(S_array)):   
        if i==0 and S_array[i]==0:
            continue
        if S_array[i]==10:
            S_array[i]='A'
        elif S_array[i]==11:
            S_array[i]='B'
        elif S_array[i]==12: 
            S_array[i]='C'
        elif S_array[i]==13:
            S_array[i]='D'
        elif S_array[i]==14:
            S_array[i]='E'
        elif S_array[i]==15:
            S_array[i]='F'
        answer=answer+str(S_array[i])

    #----------------------------------------------------------------------#

    print("SYS: Результат: ",answer)

    exit_tool=input("SYS: Программы выполнилась, нажмите кнопку для завершения")
elif a == 4:

    print("REM: при вводе переменных убедитесь что первая переменная больше второй")
    print("REM: при вводе 16х переменных используйте верхний регистр") 
    print("SYS: Какую систему исчисления использовать [2x or 10x or 16x] - ")
    sistema_4isel=int(input())     
    print("SYS: Укажите первую переменную - ")
    first_variable=str(input())     
    print("SYS: Укажите вторую переменную - ")
    second_variable=str(input())  
    res = int(first_variable) / int(second_variable)
    print('SYS: Результат: ', int(res))
    res1 = int(first_variable) % int(second_variable)
    print('SYS: Остаток: ', res1)
    

    # #----------------------------------------------------------------------#

    # len_of_1st_variable=len(first_variable)
    # len_of_2nd_variable=len(second_variable)

    # #----------------------------------------------------------------------#

    # def Switch_to_decimal(first_variable, len_of_1st_variable):
    #     first_variable=list(first_variable)
    #     for i in range(len_of_1st_variable):  
    #         if first_variable[i]=='A':
    #             first_variable[i]='10'
    #         elif first_variable[i]=='B':
    #             first_variable[i]='11'
    #         elif first_variable[i]=='C': 
    #             first_variable[i]='12'
    #         elif first_variable[i]=='D':
    #             first_variable[i]='13'
    #         elif first_variable[i]=='E':
    #             first_variable[i]='14'
    #         elif first_variable[i]=='F':
    #             first_variable[i]='15'
    #     return first_variable

    # #----------------------------------------------------------------------#

    # def Switch_to_int (first_variable, len_of_1st_variable):         
    #     for i in range(len_of_1st_variable):
    #         first_variable[i]=int(first_variable[i])

    # #----------------------------------------------------------------------#

    # def Equiv_size (stindex,exit_tool):  
    #     for i in range(exit_tool):
    #         stindex.append(0)

    # #----------------------------------------------------------------------#

    # first_variable=Switch_to_decimal(first_variable, len_of_1st_variable)
    # second_variable=Switch_to_decimal(second_variable, len_of_2nd_variable)
    # Switch_to_int(first_variable, len_of_1st_variable)
    # Switch_to_int(second_variable, len_of_2nd_variable)

    # #----------------------------------------------------------------------#

    # first_variable.reverse()
    # second_variable.reverse()

    # #----------------------------------------------------------------------#

    # if len_of_1st_variable > len_of_2nd_variable:               
    #     Equiv_size(second_variable, len_of_1st_variable-len_of_2nd_variable)

    # #----------------------------------------------------------------------#

    # T_index=0
    # array=[]
    # for i in range(len_of_1st_variable):      
    #     T_index=first_variable[i]-second_variable[i]
    #     array.append(T_index%sistema_4isel)
    #     if T_index<0:
    #         first_variable[i+1]=first_variable[i+1]-1

    # #----------------------------------------------------------------------#

    # index1=len(array)-1     
    # while array[index1]==0:
    #     array.pop()
    #     index1=index1-1
    #     if index1==-1:
    #         break
    # print('SYS: Результат: ')
    # if len(array)==0:                    
    #     print(0)
    # else:
    #     for i in range(len(array)-1, -1, -1):
    #         if array[i]==10:
    #             array[i]='A'
    #         elif array[i]==11:
    #             array[i]='B'
    #         elif array[i]==12: 
    #             array[i]='C'
    #         elif array[i]==13:
    #             array[i]='D'
    #         elif array[i]==14:
    #             array[i]='E'
    #         elif array[i]==15:
    #             array[i]='F'
    #         print(array[i])


    exit_tool=input("SYS: Программы выполнилась, нажмите кнопку для завершения")


