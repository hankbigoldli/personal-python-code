import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('300x300') #窗体宽和高
e = tk.Entry(window,show=None)
e.pack()

def insert_point():
    var = e.get()  #get()获取Entry里的信息
    t.insert('insert',var)  #插入光标所在位置
def insert_end():
    var = e.get()
    # t.insert('end',var)  #insert插入到Text中的末尾
    t.insert(1.1,var) #1.1代表插入第一行第2列  注意1
b1 = tk.Button(window,text='inset point',width=15,height=2,command=insert_point)
b1.pack()
b2 = tk.Button(window,text='inset end',width=15,height=2,command=insert_end)
b2.pack()

t = tk.Text(window,height=2)
t.pack()
window.mainloop() #窗体刷新
