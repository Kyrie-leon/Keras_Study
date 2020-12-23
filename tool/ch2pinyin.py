import os

# 图片存放的路径
path = r"G:/qingtongqi/Mid-Shang"

# 遍历更改文件名
num = 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,"Mid-Shang_"+str(num))+".jpg")
    num = num + 1