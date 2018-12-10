#！/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

import win32con
import win32api

def getin_dir(dirname):

    #“进到目录下，获取目录下的文件及文件夹”

    os.chdir(dirname)
    all_file=os.listdir("./")
    #print(all_file)
    file_list=[]
    for file in all_file:
        abs_file = dirname + "\\" + file
        #print(abs_file)    

        if os.path.isfile(abs_file):
            #print("%s is a file,will append in file_list" % abs_file)
            file_list.append(abs_file)
            
        elif os.path.isdir(abs_file):
            #print("%s is a dir, will recall in getin_dir()" % abs_file)
            getin_dir(abs_file)
        
    print("当前目录下的file_list is %s" % file_list)

    for file in file_list:
        
        win32api.SetFileAttributes(file,win32con.FILE_ATTRIBUTE_NORMAL)
        #修改文件的属性为normal，（可以readonly,hidden）

        rename_file(file)

        
def rename_file(absfile):

    #“修改单个文件的名字，先获取文件名字要删掉的内容

    abs_dir,filename1 = os.path.split(absfile)
    file_name,expend_name = os.path.splitext(filename1)
    new_name = ""
    for i in file_name:
        if i == "(":
            break
        else:
            new_name+=i
    print(new_name)
    new_file_name = abs_dir+"\\"+new_name[0:-1]+expend_name
    print(new_file_name)

    os.rename(absfile,new_file_name)    


if __name__ == "__main__":
    need_dir = input("Please input the abs_path_name:___(For example:e:\python\work-scripts\12-7\)")
    getin_dir(need_dir)

