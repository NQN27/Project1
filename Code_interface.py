#Thêm thư viện tkinter
from tkinter import *
from tkinter import messagebox
from test_class import name
import folium
from tkinter import Tk, Label, Button
import webbrowser

def show_map(m):
    root = Tk()
    root.title('Show directions map')
    root.geometry('200x100')
    def show_map():
        m.save('map.html')
        webbrowser.open_new('map.html')
        root.destroy()
    button = Button(root, text="Show Map", command=show_map)
    button.pack()
    root.mainloop()
def Call_interface():

    top = Tk()
    top.title('DIRECTOR')
    top.geometry("400x250")
    
    Start = Label(top, text = "Start").place(x = 30, y = 50)
    End = Label(top, text = "End").place(x = 30, y = 90)
    start_point=StringVar()
    end_point=StringVar()
    e1 = Entry(top,textvariable=start_point).place(x = 80, y = 50)
    e2 = Entry(top,textvariable=end_point).place(x = 80, y = 90)
    def clicked():
        if selected.get() == 0:
            messagebox.showwarning('NOT CHOOSE TYPE INPUT YET', 'Please selected one')
        else:
            global a,b,c
            a,b,c=start_point.get(),end_point.get(),selected.get()
            top.destroy()
    selected = IntVar()
    
    rad1 = Radiobutton(top,text='Input place_name', value=1, variable=selected)
    rad2 = Radiobutton(top,text='Input coordinates', value=2, variable=selected) 
    btn = Button(top, text="Submit", bg="white", fg="red",command=clicked)

    rad1.grid(column=0, row=0)
    rad2.grid(column=1, row=0)  
    #Thiết lập vị trí của nút nhấn có màu nền và màu chữ
    btn.place(x=250, y=65)
    #Vị trí xuất hiện của Textbox
    top.mainloop()
    return a,b,c
def Call_interface2():

    top = Tk()
    top.title('DIRECTOR')
    top.geometry("400x250")
    
    Start = Label(top, text = "Start").place(x = 30, y = 50)
    End = Label(top, text = "End").place(x = 30, y = 90)
    start_point=StringVar()
    end_point=StringVar()
    e1 = Entry(top,textvariable=start_point).place(x = 80, y = 50)
    e2 = Entry(top,textvariable=end_point).place(x = 80, y = 90)
    def clicked():
        global a,b
        a,b=start_point.get(),end_point.get()
        if a not in name or b not in name:
            messagebox.showwarning('WRONG NAME', 'Please write corect name of the city like HaNoi,HoChiMinhCity')
        else:
            top.destroy()
    btn = Button(top, text="Submit", bg="white", fg="red",command=clicked)

    #Thiết lập vị trí của nút nhấn có màu nền và màu chữ
    btn.place(x=250, y=65)
    #Vị trí xuất hiện của Textbox
    top.mainloop()
    return a,b





#Lặp vô tận để hiển thị cửa sổ
