import cv2

# 读取原始图像
image = cv2.imread('chessboard.png')

# 压缩图像至600x600尺寸
resized_image = cv2.resize(image, (600, 600))

# 定义每个小格子的尺寸
cell_width = resized_image.shape[1] // 8
cell_height = resized_image.shape[0] // 8

coordinate = None
window_name = None

while True:
    # 请求输入要提取的区域坐标
    coordinate = input("请输入要提取的区域坐标（例如a1, e3, e4），输入q退出：")

    # 检查是否输入退出命令
    if coordinate.lower() == 'q':
        break

    # 检查输入的坐标是否合法
    if len(coordinate) != 2 or coordinate[0] < 'a' or coordinate[0] > 'h' or coordinate[1] < '1' or coordinate[1] > '8':
        print("无效的坐标，请重新输入！")
        continue

    if window_name is not None:
        cv2.destroyWindow(window_name)

    # 解析坐标
    column = ord(coordinate[0]) - ord('a')
    row = int(coordinate[1]) - 1

    # 计算区域的边界
    x_start = column * cell_width
    y_start = row * cell_height
    x_end = x_start + cell_width
    y_end = y_start + cell_height

    # 提取指定区域的图像
    cell_image = resized_image[y_start:y_end, x_start:x_end]


    # 生成新窗口名称，并显示提取的图像
    window_name = coordinate
    cv2.imshow(window_name, cell_image)

cv2.destroyAllWindows()




