import os
import re
import time
import pickle
file_list = os.listdir(os.getcwd())
print(file_list)
name_list = []
data_list = []
#获取JPG文件
for item in file_list:
    file_name,file_suffix = item.split('.')
    if file_suffix == 'jpg':
        name_list.append(file_name)
#分割JPG文件,获取时间戳和姓名
for temp in name_list:
    num = re.findall(r'\d+', temp)
    gender = temp[-1:]
    print(temp)
    print(num)
    print('gender' + gender)
    # name = re.findall(r'[\u4e00-\u9fa5][\u4e00-\u9fa5]',temp) #匹配人名
    name_all = re.findall(r'[\u4e00-\u9fa5]+',temp) #匹配人名

    name = name_all[0][0:len(name_all[0])]

    print(name)
    st = time.localtime(int(num[0]))
    date = time.strftime('%Y-%m-%d', st) #时间戳转时间

    data_list.append((name[0],gender,date,"\\药方查询\\"+temp+'.jpg'))

    # print(list(filter(str.isdigit,temp)))
print(data_list)
print(os.getcwd())
save_file = open(os.getcwd()+"\\data.xxx",'wb+')
pickle.dump(data_list, save_file)
save_file.close()
