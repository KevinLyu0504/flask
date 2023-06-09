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

# 加载第一张图片
image1 = cv2.imread('chessboard.png')

# 调整第一张图片尺寸为 400x400 像素
resized_image1 = resize_image(image1, (400, 400))

# 加载第二张图片
image2 = cv2.imread('chessboard1.png')

# 调整第二张图片尺寸为 400x400 像素
resized_image2 = resize_image(image2, (400, 400))

# 计算差异图像
diff_image = cv2.absdiff(resized_image1, resized_image2)

# 将差异图像转换为灰度图像
gray_diff_image = cv2.cvtColor(diff_image, cv2.COLOR_BGR2GRAY)

# 对差异图像应用阈值处理
_, threshold_image = cv2.threshold(gray_diff_image, 30, 255, cv2.THRESH_BINARY)

# 轮廓提取
contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

chess_moves = []

# 遍历轮廓并输出移动位置
for contour in contours:
    # 计算轮廓的边界框
    x, y, w, h = cv2.boundingRect(contour)
    # 计算棋子所在方格的索引
    start_col = chr(ord('a') + x // (400 // 8))
    start_row = str(8 - y // (400 // 8))
    # 将移动位置存储到列表中
    chess_moves.append((start_col, start_row))

print(chess_moves)

# 输出移动位置
if len(chess_moves) == 2:
    start_col, start_row = chess_moves[0][0], chess_moves[0][1]
    end_col, end_row = chess_moves[1][0], chess_moves[1][1]
    print(f"棋子从坐标 ({start_col}{start_row}) 移动到 ({end_col}{end_row})")
else:
    print("无效的移动")



# 显示第二张图片和绘制的坐标
locate_chessboard(resized_image2)
