from tkinter import *
import customtkinter as c

c.set_appearance_mode('dark')
root = c.CTk()
c.set_default_color_theme('blue')
root.geometry('400x600')

from func_for_main import *

root.title('maths aip')


def clear():
    for i in root.winfo_children():
        i.destroy()


# delete dup start
def dele():
    clear()
    l = c.CTkLabel(root, text='''--DUPLICATES--
    enter the set in the given entery box like this
    {1,2,3,4,5,6,7} and press submit 
    (currently limited to int and decimal values)''', font=('Comic Sans MS', 18)).pack()

    def jk():
        d.pack()
        g = e.get()
        g = ld(g)
        d.configure(text=f'your set after deletion is : {delete(g)}')

    def cl():
        dele()

    e = c.CTkEntry(root, placeholder_text='type here', height=50, width=200, font=('Calibri', 18))
    d = c.CTkLabel(root, text='', width=200, height=180, font=('Comic Sans MS', 18))
    e.pack()
    b = c.CTkButton(root, text='submit', command=jk, font=('Calibri', 15)).pack(pady=7)
    cl = c.CTkButton(root, text='clear', command=cl, font=('Calibri', 15)).pack(pady=7)
    m = c.CTkButton(root, text='main menu', command=main, font=('Calibri', 15)).pack(pady=7)


# delete dup end
# union start
def u():
    clear()
    l = c.CTkLabel(root, text='''--UNION--
    enter the set in the given entery box like this
    {1,2,3,4,5,6,7} and press submit 
    (currently limited to int and decimal values)''', font=('Comic Sans MS', 18)).pack()

    def ju():
        d.pack()
        g = e1.get()
        g = ld(g)
        o = f1.get()
        o = ld(o)
        g = union(g, o)

        d.configure(text=f'UNION : {delete(g)}')

    def cl():
        u()

    e1 = c.CTkEntry(root, placeholder_text='set 1', height=50, width=200, font=('Calibri', 18))
    f1 = c.CTkEntry(root, placeholder_text='set 2', height=50, width=200, font=('Calibri', 18))
    e1.pack()
    f1.pack()
    d = c.CTkLabel(root, text='', width=200, height=180, font=('Comic Sans MS', 18))
    b = (c.CTkButton(root, text='submit', command=ju, font=('Calibri', 15)).pack(pady=7))
    cl = c.CTkButton(root, text='clear', command=cl, font=('Calibri', 15)).pack(pady=7)
    m = c.CTkButton(root, text='main menu', command=main, font=('Calibri', 15)).pack(pady=7)


# union end

# inter start
def intr():
    clear()
    l = c.CTkLabel(root, text='''--INTERSECTION--
    enter the set in the given entery box like this
    {1,2,3,4,5,6,7} and press submit 
    (currently limited to int and decimal values)''', font=('Comic Sans MS', 18)).pack()

    def ju():
        d.pack()
        g = e1.get()
        g = ld(g)
        o = f1.get()
        o = ld(o)
        g = inter(list1=g, list2=o)
        d.configure(text=f'INTERSECT : {g}')

    def cl():
        intr()

    e1 = c.CTkEntry(root, placeholder_text='set 1', height=50, width=200, font=('Calibri', 18))
    f1 = c.CTkEntry(root, placeholder_text='set 2', height=50, width=200, font=('Calibri', 18))
    e1.pack()
    f1.pack()
    d = c.CTkLabel(root, text='', width=200, height=180, font=('Comic Sans MS', 18))
    b = (c.CTkButton(root, text='submit', command=ju, font=('Calibri', 15)).pack(pady=7))
    cl = c.CTkButton(root, text='clear', command=cl, font=('Calibri', 15)).pack(pady=7)
    m = c.CTkButton(root, text='main menu', command=main, font=('Calibri', 15)).pack(pady=7)


# inter end

# subset start
def sub():
    clear()
    l = c.CTkLabel(root, text='''--SUBSET CHECKER--
    enter the set in the given entery box like this
    {1,2,3,4,5,6,7} and press submit 
    (currently limited to int and decimal values)''', font=('Comic Sans MS', 18)).pack()

    def ju():
        d.pack()
        g = e1.get()
        g = ld(g)
        o = f1.get()
        o = ld(o)
        g = ch(g, o)
        d.configure(text=f'RESULT : {g}')

    def cl():
        sub()

    e1 = c.CTkEntry(root, placeholder_text='superset', height=50, width=200, font=('Calibri', 18))
    f1 = c.CTkEntry(root, placeholder_text='subset', height=50, width=200, font=('Calibri', 18))
    e1.pack()
    f1.pack()
    d = c.CTkLabel(root, text='', width=200, height=180, font=('Comic Sans MS', 18))
    b = (c.CTkButton(root, text='submit', command=ju, font=('Calibri', 15)).pack(pady=7))
    cl = c.CTkButton(root, text='clear', command=cl, font=('Calibri', 15)).pack(pady=7)
    m = c.CTkButton(root, text='main menu', command=main, font=('Calibri', 15)).pack(pady=7)


# sub end

# set diff start

def di():
    clear()
    l = c.CTkLabel(root, text='''--SET DIFFERENCE--
    enter the set in the given entery box like this
    {1,2,3,4,5,6,7} and press submit 
    (currently limited to int and decimal values)''', font=('Comic Sans MS', 18)).pack()

    def ju():
        d.pack()
        g = e1.get()
        g = ld(g)
        o = f1.get()
        o = ld(o)
        g = setd(g, o)
        d.configure(text=f'RESULT : {g}')

    def cl():
        di()

    e1 = c.CTkEntry(root, placeholder_text='A', height=50, width=200, font=('Calibri', 18))
    f1 = c.CTkEntry(root, placeholder_text='B', height=50, width=200, font=('Calibri', 18))
    e1.pack()
    f1.pack()
    warn = c.CTkLabel(root, text='A-B', font=('Comic Sans MS', 18)).pack()
    d = c.CTkLabel(root, text='', width=200, height=180, font=('Comic Sans MS', 18))
    b = (c.CTkButton(root, text='submit', command=ju, font=('Calibri', 15)).pack(pady=7))
    cl = c.CTkButton(root, text='clear', command=cl, font=('Calibri', 15)).pack(pady=7)
    m = c.CTkButton(root, text='main menu', command=main, font=('Calibri', 15)).pack(pady=7)


# set diff end

# grp start

def grp():
    clear()
    l = c.CTkLabel(root, text='''--MORE INFO--
CREATED BY JIDU IN PYTHON
USING CUSTOM TKINTER AND
 TKINTER MODULES''', font=('Comic Sans MS', 18)).pack()
    m = c.CTkButton(root, text='main menu', font=('Comic Sans MS', 24), command=main, height=70, width=200).pack(
        pady=200)


# grp end


# main
def main():
    clear()
    l = c.CTkLabel(root, text='SET CALCULATOR --DEV -JIDU', height=100, width=200, font=('Comic Sans MS', 18)).pack(
        padx=5, pady=10)
    delet = c.CTkButton(root, text='delete duplicate elements', width=120, height=50, command=dele,
                        font=('Comic Sans MS', 18)).pack(padx=5, pady=10)
    union = c.CTkButton(root, text='union', width=120, height=50, font=('Comic Sans MS', 18), command=u).pack(padx=5,
                                                                                                              pady=10)
    instersect = c.CTkButton(root, text='intersection', width=120, height=50, command=intr,
                             font=('Comic Sans MS', 18)).pack(padx=5, pady=10)
    ch = c.CTkButton(root, text='subset checker', command=sub, width=120, height=50, font=('Comic Sans MS', 18)).pack(
        padx=5, pady=10)
    diff = c.CTkButton(root, text='set diff', width=120, height=50, command=di, font=('Comic Sans MS', 18)).pack(padx=5,
                                                                                                                 pady=10)
    group = c.CTkButton(root, text='more info', command=grp, width=120, height=50, font=('Comic Sans MS', 18)).pack(
        padx=5, pady=10)


if __name__ == '__main__':
    main()
    root.mainloop()
