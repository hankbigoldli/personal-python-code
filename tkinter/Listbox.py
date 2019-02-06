import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('300x300') #窗体宽和高
var1 = tk.StringVar()

l = tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b = tk.Button(window,text='print selection',width=15,height=2,command=print_selection)
b.pack()
var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window,listvariable=var2,)
list_items = [1,2,3,4,3,3,3,3,3,3,3,3,3]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'two')
lb.delete(2)
lb.pack()


window.mainloop() #窗体刷新