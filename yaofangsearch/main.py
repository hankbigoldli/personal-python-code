'''
by: hankli

'''

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog  #打开文件对话框
from tkinter import  messagebox
import datetime
import time
import pickle
from PIL import Image as imm
import os,os.path

#主体构建
window = tk.Tk()
window.title('药方存根查询 v1.2           by:lihan')
window.geometry('405x410')
search_entry_text = tk.StringVar()
data_List = []  #存放全部数据
#左键双击事件
def view_list_doubleClick(event):

    item_text = view_list.item(view_list.selection()[0],'values')
    # print(item_text)
    img = imm.open(os.getcwd()+item_text[3])
    img.show()
#获取当前列表信息戳
def ac_allinfo_view():
    t = view_list.get_children()
    return t
#显示全部信息
def display_all():
    del_view_list(ac_allinfo_view()) #清屏
    for temp_display in data_List:
        view_list.insert('',0,values=temp_display)
#view_list清空
def del_view_list(t):
    for del_view_list_temp in t:
        view_list.delete(del_view_list_temp)
#查找数据
def search_info():
    temp_search = []  # 存放符合条件的数据
    var_search_entry = search_entry_text.get()
    #查找符合条件的数据
    for final in data_List:
        print(final)
        if var_search_entry == final[0]:
            temp_search.append(final)

    if not temp_search:
        messagebox.showerror(title='Error',message='查无此人！')
    else:
        print(temp_search)
        del_view_list(ac_allinfo_view())#清屏

        for data_temp_search in temp_search:
            view_list.insert('',0,values=data_temp_search)

#生成子窗口
def add_info_create():
    add_win = tk.Toplevel()
    add_win.title('信息添加')
    add_win.geometry('350x200')
    new_addr = []
    pict_addr = tk.StringVar() #图片地址类
    var_entry_name = tk.StringVar() #姓名类
    var_entry_gender = tk.StringVar() #性别类
    def open_file():
        picture_addr = filedialog.askopenfilename(title='加载药方图片',filetypes=[('JPG','*.jpg'),('PNG','*.png'),('All Files','*')])
        pict_addr.set(picture_addr)
    def move_file():
        im_addr = pict_addr.get() #获取图片地址赋值给变量
        im = imm.open(str(im_addr))  #打开图片文件
        var_name = var_entry_name.get()   #获取用户名
        var_gender = var_entry_gender.get() #获取性别
        temp_time = str(time.time()).split('.',1)[0]
        addr = '\\药方存根\\'+temp_time+str(var_name)+str(var_gender)+'.jpg'
        im.save(os.getcwd()+addr)
        new_addr.append(addr)
    def add_info():
        move_file()
        #信息不为空
        if (var_entry_name.get()  in '') or (var_entry_gender.get()  in '') or (pict_addr.get()  in ''):
            messagebox.showerror(title='Error', message='内容不能为空!')
        else:
            view_list.insert('', 0, values=(str(var_entry_name.get()), str(var_entry_gender.get()), str(datetime.datetime.now().strftime('%Y-%m-%d')), str(new_addr[0])))
            data_List.insert(0,(str(var_entry_name.get()), str(var_entry_gender.get()), str(datetime.datetime.now().strftime('%Y-%m-%d')), str(new_addr[0])))
            messagebox.showinfo(title='Successful',message='信息添加成功！')
            add_win.destroy() #销毁子窗口

    #子窗口部件构建
    add_info_label_name = tk.Label(add_win, text='姓名', font=('微软雅黑', 11, 'normal')).place(x=50, y=4)
    add_info_label_gender = tk.Label(add_win, text='性别', font=('微软雅黑', 11)).place(x=50, y=50)
    add_info_label_pictureaddr = tk.Label(add_win, text='药方地址', font=('微软雅黑', 11)).place(x=15, y=96)
    add_info_entry_name = tk.Entry(add_win, show=None,text=var_entry_name).place(x=90, y=10)
    add_info_entry_gender = tk.Entry(add_win, show=None,text=var_entry_gender).place(x=90, y=55)
    add_info_entry_pictureaddr = tk.Entry(add_win,show=None,textvariable=pict_addr,state='disabled').place(x=90, y=100)
    add_info_button_picture = tk.Button(add_win,text='添加图片',command=open_file).place(x=275,y=95)
    add_info_button = tk.Button(add_win,text='添加',width=10,command=add_info).place(x=120,y=150)
#主窗口销毁事件
def on_closing():
    if messagebox.askokcancel("Quit","是否要退出？"):
        save_file = open(os.getcwd()+'\\药方存根\\'+'data.xxx','wb+')
        pickle.dump(data_List, save_file)
        save_file.close()
        window.destroy()
'''
主体窗口部件构建
'''
# 搜索框
search_entry = tk.Entry(window,width=15,show=None,textvariable=search_entry_text).place(x=10,y=12)
# 搜索按钮
search_button = tk.Button(window,text='搜索',width=6,command=search_info).place(x=160,y=8)
#添加信息按钮
add_button = tk.Button(window,text='添加',width=6,command=add_info_create).place(x=235,y=8)
#显示全部信息
viewall_button = tk.Button(window,text='显示全部',width=7,command=display_all).place(x=310,y=8)
#构建显示列表
view_list = ttk.Treeview(window,height=16,columns=('姓名','性别','时间','药方图片地址'),show='headings')
view_list.column('姓名',width=60,anchor='center')
view_list.column('性别',width=45,anchor='center')
view_list.column('时间',width=95,anchor='center')
view_list.column('药方图片地址',width=170,anchor='center')
view_list.heading('姓名',text='姓名')
view_list.heading('性别',text='性别')
view_list.heading('时间',text='时间')
view_list.heading('药方图片地址',text='药方图片地址')
view_list.place(x=10,y=55)
#显示列表添加竖直滚动条
vbar = ttk.Scrollbar(window,orient=tk.VERTICAL,command=view_list.yview)
view_list.configure(yscrollcommand=vbar.set)
vbar.pack(side=tk.RIGHT,fill=tk.Y)
#创建存储药方图片的目录并载入数据
if not os.path.exists(os.getcwd()+'\\药方存根'):
    os.mkdir(os.getcwd()+'\\药方存根')
else:
    read_file = open(os.getcwd()+'\\药方存根\\'+'data.xxx','rb')
    var = pickle.load(read_file)
    for i in range(len(var)):
        view_list.insert('',0,values=var[i])
        data_List.append(var[i])


view_list.bind('<Double-Button-1>',view_list_doubleClick)



window.protocol("WM_DELETE_WINDOW",on_closing)
window.mainloop()
