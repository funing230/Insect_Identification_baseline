#coding=utf-8
# 需要注意的是，经过resize的预处理会使得昆虫原有的形态特征发生变化，不利于后期的比较

import os
import cv2

path = "./dataset"
files = os.listdir(path)


for filename in files: #遍历文件夹
     if not os.path.isdir(filename): #判断是否是文件夹，不是文件夹才打开
         print (filename)
         img = cv2.imread("./dataset/" + filename)
         img2 = cv2.resize(img,(200,200))
         cv2.imwrite("E./processedData/" + filename,img2)