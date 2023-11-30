import cv2
import numpy as np


def enhance_license_plate(image_path):
    # 读取图片
    image = cv2.imread(image_path)

    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用高斯模糊
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 使用自适应阈值进行二值化
    binary = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # 边缘检测
    edges = cv2.Canny(binary, 100, 200)

    # 对边缘图像进行膨胀操作，以突出车牌号码
    dilated = cv2.dilate(edges, np.ones((3, 3), np.uint8), iterations=1)

    # 显示结果
    image = cv2.resize(image, None, fx=0.5, fy=0.5)
    cv2.imshow('Original Image', image)
    dilated = cv2.resize(dilated, None, fx=0.5, fy=0.5)
    cv2.imshow('Enhanced License Plate', dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 使用图片路径调用函数
enhance_license_plate('../dataset/test1111.jpg')
