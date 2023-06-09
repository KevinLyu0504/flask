import cv2
import numpy as np

def resize_image(image, size):
    return cv2.resize(image, size)

def locate_chessboard(image):
    # 将图像转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 棋盘大小
    board_size = (8, 8)

    # 计算每个方格的大小
    square_size = (image.shape[1] // board_size[0], image.shape[0] // board_size[1])

    # 绘制棋盘方格和坐标
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            x = i * square_size[0] + square_size[0] // 2
            y = j * square_size[1] + square_size[1] // 2
            cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
            cv2.putText(image, f'{chr(i + 97)}{board_size[1] - j}', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # 显示结果图像
    cv2.imshow('Chessboard', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 加载图像
image = cv2.imread('chessboard.png')

# 调整图像尺寸为 400x400 像素
resized_image = resize_image(image, (400, 400))

# 调用函数定位棋盘并显示坐标
locate_chessboard(resized_image)
