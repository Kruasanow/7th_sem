import math
from tkinter import Tk, Entry, W, E, Label, Button

window = Tk()
window.title('Proga')

enta = Entry(window, width=60)
enta.grid(row=1, columnspan=5, padx = 5, pady = 5, sticky=W+E)

entb = Entry(window)
entb.grid(row=2, columnspan=5, padx = 5, pady = 5, sticky=W+E)

res = Label(window, text = '')
res.grid(row=4, columnspan=5, padx = 5, pady = 5, sticky=W+E)

def bEvc():
    a = int(enta.get())
    b = int(entb.get())
    r = Evclid(a,b)
    res.config(text = str(r))

def Evclid(a, b):
    if b>a:
        c = a
        a = b
        b = c
    while b!=0:
        c = a % b
        a = b
        b = c
    return a

def bREvc():
    a = int(enta.get())
    b = int(entb.get())
    r = R_Evclid(a,b)
    t = str(Evclid(a,b)) + ' = ' + str(a) + '*(' + str(r[0]) + ') + ' + str(b) + '*(' + str(r[1]) + ')'
    res.config(text = t)

def R_Evclid(ax, b):
    AX = ax
    B = b
    if b>ax:
        c = ax
        ax = b
        b = c
    x = [1, 0]
    y = [0, 1]
    a = [ax, b]
    while a[1] != 0:
        q = a[0] // a[1]
        c = a[0]
        a[0] = a[1]
        a[1] = c - a[1]*q
        c = x[0]
        x[0] = x[1]
        x[1] = c - x[1]*q
        c = y[0]
        y[0] = y[1]
        y[1] = c - y[1]*q
    if B > AX:
        result = [y[0], x[0]]
    else:
        result = [x[0], y[0]]
    return result

def bEuler():
    a = int(enta.get())
    r = Euler(a)
    res.config(text = str(r))

def Euler(x):
    A = []
    for i in range(2, int(x**(math.sqrt(1/2)))):
        if x % i != 0:
            continue
        k = 0
        while x % i == 0:
            x = x//i
            k += 1
        A.append([i,k])
    p = 1
    for i in range(len(A)):
        p = p*(A[i][0]**A[i][1] - A[i][0]**(A[i][1] - 1))

    return p

def bLeg():
    a = int(enta.get())
    b = int(entb.get())
    r = 'L('+ str(a) + ',' + str(b) + ')= ' + str(Leg(a,b))
    res.config(text = r)

def Leg(a,b):
    if a % b == 0:
        return 0
    if a**((b-1)/2) % b == 1:
        return 1
    else:
        return -1
    
def bJakob():
    a = int(enta.get())
    b = int(entb.get())
    r = 'J(' + str(a) + ',' + str(b) + ')= ' + str(Jakob(a,b))
    res.config(text = r)

def Jakob(a, m):
    A = []
    P = 1
    for i in range(2, int(a**(math.sqrt(1/2)))):
        if a % i != 0:
            continue
        k = 0
        while a % i == 0:
            a = a//i
            k += 1
        P = P*(Leg(a,i))**k
        A.append([i,k])
    return P

btnE = Button(window, text = 'НОД', command=bEvc)
btnE.grid(row=3, column=0, padx = 5, pady = 5, sticky=W+E) 

btnEr = Button(window, text = 'ЛинПредст', command=bREvc)
btnEr.grid(row=3, column=1, padx = 5, pady = 5, sticky=W+E)

btnEu = Button(window, text = 'Ф Эйлера', command= bEuler)
btnEu.grid(row=3, column=2, padx = 5, pady = 5, sticky=W+E)

btnL = Button(window, text = 'сЛежандра', command=bLeg)
btnL.grid(row=3, column=3, padx = 5, pady = 5, sticky=W+E)

btnJ = Button(window, text = 'сЯкоби', command=bJakob)
btnJ.grid(row=3, column=4, padx = 5, pady = 5, sticky=W+E)

window.mainloop()
