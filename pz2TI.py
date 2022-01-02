from tkinter import *
from tkinter import filedialog, messagebox
import math
import re
import os
#----------------------------------------------------------------------------#
bits_array =""
buffer = []
def open_dir_finc():
    #----------------------------------------------------------------------------#
    global file_open_trace
    global bits_array
    global buffer
    #----------------------------------------------------------------------------#
    file_list = [('Все файлы','*'),('Excel','csv')]
    file_open = filedialog.askopenfile(filetypes = file_list)
    file_open_trace = file_open.name
    file = open(file_open_trace,'rb')
    buffer = file.read(1024*1024)
    file.close()
    #----------------------------------------------------------------------------#
    for i in buffer:
        bits_array += str(bin(i))[2:]
    #----------------------------------------------------------------------------#
def get_number_of_bits(choosed_number):
    global number_of_bits 
    global bits_array
    global buffer
    Hcurrent = 0
    number_of_bits = int(choosed_number)

    input_number = number_of_bits

    bits_array = re.findall(r'\d'*input_number, bits_array)

    udovl_sob = list(set(bits_array))

    #----------------------------------------------------------------------------#
    Vmatrix = [[0] * len(udovl_sob) for i in range(len(udovl_sob))]
    
    for i in range(0, len(bits_array)-1):
        Vmatrix[udovl_sob.index(bits_array[i])][udovl_sob.index(bits_array[i+1])] += 1
    
    for i in range(len(Vmatrix)):
        for j in range(len(Vmatrix)):
            Vmatrix[i][j] /= len(bits_array) 
            if Vmatrix[i][j] != 0:
                Hcurrent += Vmatrix[i][j]*math.log2(Vmatrix[i][j])
    #----------------------------------------------------------------------------#
    Hcurrent = (-1)*Hcurrent

    Hmaximum = 2*math.log2(len(udovl_sob))

    Hled = Hcurrent/Hmaximum
    #----------------------------------------------------------------------------#
    FileVerMatr = open('Vmatrix.csv','w+')
    FileVerMatr.write('                    ')
    for i in udovl_sob:
        FileVerMatr.write(i + '                     ')
    FileVerMatr.write('\n')
    for i in range(0, len(udovl_sob)):
        FileVerMatr.write(udovl_sob[i] + '          ')
        for j in range(0, len(udovl_sob)):
            FileVerMatr.write(str(Vmatrix[i][j])+'     ')
        FileVerMatr.write('\n')
    FileVerMatr.close()
    os.startfile('Vmatrix.csv')
    #----------------------------------------------------------------------------#
    Label(text=str(Hmaximum)).place(x=5, y=100)
    Label(text=str(Hcurrent)).place(x=5, y=180)
    Label(text=str(Hled)).place(x=5, y=260)
#----------------------------------------------------------------------------#
Window = Tk()
Window.title("pz2_TI_Rusanow")
Window.geometry('300x300')
Window['bg'] = "#3300FF"
#----------------------------------------------------------------------------#
messagebox.showwarning('Предисловие', 'при вводе длины символа, необходимо, чтобы число n удовлетворяло условию: input_number(n)<=8')
btnOpen = Button(Window, text="Выбрать файл",command=open_dir_finc,width = 12, height= 1,bg='black', fg="white").place(x=5, y=20)
btnN = Button(Window, text="Показать результат",command=lambda:get_number_of_bits(entry_text.get()),width = 15, height= 1,bg='black', fg="white").place(x=170, y=20)
PrintHmax = Label(Window, text= "Максимальная энтропия", font=('Times New Roman',18)).place(x=5, y=60)
PrintHtec = Label(Window, text= "Текущая энтропия", font=('Times New Roman',18)).place(x=5, y=140)
PrintHpriv = Label(Window, text="Приведенная энтропия", font=('Times New Roman',18)).place(x=5, y=220)
entry_text = StringVar()
choosed_number = Entry(Window,width=11,textvariable = entry_text).place(x=100, y=24)

Window.mainloop()

