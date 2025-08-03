import cv2
import numpy as np

image=cv2.imread(R"D:\Python_pro\Open_CV\test_images\saidao.jpeg")
image_hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# 定义黄色范围（需要根据实际情况调整）
lower_yellow = np.array([15, 100, 100])  # 较低阈值
upper_yellow = np.array([35, 255, 255])  # 较高阈值

mask=cv2.inRange(image_hsv,lower_yellow,upper_yellow)

# 形态学操作：去噪和填充空洞
kernel = np.ones((5, 5), np.uint8)
'''
去除图像中干扰项
mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE , kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE , kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE  , kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE , kernel)
'''
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN , kernel)
cv2.imshow("test2",mask)


# 检测轮廓
contours, _= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, contours, 0, (0, 0, 255), 1)

cv2.imshow('Racecourse Detection', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
