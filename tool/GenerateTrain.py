import os

folder_path = '.\VOCdevkit\VOC2007\JPEGImages\data'  #文件路径
num = 1

if __name__ == '__main__':
    for file in os.listdir(folder_path):
        s = '%04d' % num  # 04表示0001,0002等命名排序
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, str(s) + '.jpg')) #图片格式
        num += 1
