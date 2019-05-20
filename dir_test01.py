import os

def all_path(dirname):

    result = []#所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        print("1:",maindir) #当前主目录
        print("2:",subdir) #当前主目录下的所有目录
        print("3:",file_name_list)  #当前主目录下的所有文件

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            result.append(apath)

    return result

print(all_path("c:\Autel_2019_01_07"))