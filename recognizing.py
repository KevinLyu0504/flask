import cv2
import numpy as np

# 读取图像
image = cv2.imread('blank1.png')

# 转换为HSV颜色空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



lower_white = np.array([0, 0, 200], dtype=np.uint8)
upper_white = np.array([180, 30, 235], dtype=np.uint8)


lower_black = np.array([0, 0, 0], dtype=np.uint8)
upper_black = np.array([180, 255, 50], dtype=np.uint8)


white_mask = cv2.inRange(hsv_image, lower_white, upper_white)
white_mask_image = cv2.bitwise_and(image, image, mask=white_mask) #可视化
white_pixels = cv2.countNonZero(white_mask)
print(white_pixels)


black_mask = cv2.inRange(hsv_image, lower_black, upper_black)
black_mask_image = cv2.bitwise_and(image, image, mask=black_mask)
black_pixels =cv2.countNonZero(black_mask)
print(black_pixels)





if white_pixels != 0 or black_pixels != 0:
    if white_pixels > black_pixels:
        print("棋子为白色")
    elif black_pixels > white_pixels:
        print("棋子为黑色")
else:
    print("棋盘为空")
