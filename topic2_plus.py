import cv2
import numpy as np


def get_contuner(image):
    #image = cv2.imread(r"D:\Python_pro\Open_CV\test_images\saidao_2.png")

    # 转换为HSV颜色空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义黄色范围（需要根据实际情况调整）
    lower_yellow = np.array([15, 100, 100])  # 较低阈值
    upper_yellow = np.array([35, 255, 255])  # 较高阈值

    # 创建掩码
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    '''
    掩码是黑白的,即二wei的
    '''

    # 形态学操作：去噪和填充空洞
    kernel = np.ones((5, 5), np.uint8)
    '''
    去除图像中干扰项
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE , kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE , kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE  , kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE , kernel)
    '''
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cv2.imshow("test2", mask)

    """
    cv2.imwrite(r"D:\Python_pro\Open_CV\test_images\test1_mask.png",mask)
    """

    # 检测轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 筛选轮廓（根据面积等条件）
    '''
    max_contour = max(contours, key=cv2.contourArea)
    '''
    # 绘制轮廓
    # cv2.drawContours(image, contours, 0, (0, 0, 255), 1)

    '''
    #  矩形包围框
    x,y,w,h = cv2.boundingRect(contours[0])
    brcnt = np.array([[[x, y]], [[x+w, y]], [[x+w, y+h]], [[x, y+h]]])
    cv2.drawContours(image, [brcnt], -1, (255, 255,255), 2)
    '''

    # 逼近多边形
    epsilon = 0.055 * cv2.arcLength(contours[0], True)
    approx = cv2.approxPolyDP(curve=contours[0], epsilon=epsilon, closed=True)
    #cv2.drawContours(image, [approx], 0, (0, 0, 255), 2)

    return approx


#____
def fun_goTo_center(image,step=10,start_x=100,strat_y=300,vertical_w=0.5):   #vertical_w-->竖直方向的权重，默认为0.5

#权重分配
    assert vertical_w <= 1.0 ,"权重分配超出范围（>1）"
    assert vertical_w >= 0.0 ,"权重分配超出范围（<0）"
    horizontal_w=1-vertical_w   #horizontal-->水平方向的权重
#_____________
    shape = image.shape
    color_c=tuple(image[300,100])
    print(color_c)
# get r
    i = 100
    for i in range(100, 200, 1):
        a, b, c = image[300, i]
        if a != 36:
            r = i - 100  # r-->红圈的半径
            print(r)
            break

#__
    aim_x=0;aim_y=0
    for i in range(0,4):
        aim_x+=approx[i][0,0]//4
        aim_y+=approx[i][0,1]//4


    step_x=abs(aim_x-start_x)//step
    step_y=abs(aim_y-strat_y)//step

    degree_x=0;degree_y=0

    temp_x=start_x;temp_y=strat_y
    trajectory=[(temp_x,temp_y)]

    total_step=step_x+step_y
    for _ in range(0,total_step,1):
        if horizontal_w*(1-degree_x/step_x)>=vertical_w*(1-degree_y/step_y):
            temp_x+=10;degree_x+=1
        else:
            temp_y-=10;degree_y+=1

        trajectory.append((temp_x,temp_y))

    image_c=image.copy()
    cv2.circle(image_c,trajectory[total_step],radius=r,color=[36,28,237],thickness=-1)
    for i in range(0, total_step, 1):
        cv2.line(image_c, trajectory[i], trajectory[i + 1], color=[0, 0, 0], thickness=2)
    cv2.imshow('over', image_c)



#__________________
if __name__=='__main__':
  image=cv2.imread(r"D:\Python_pro\Open_CV\test_images\saidao_2.png")
  approx = get_contuner(image)
  x=float(input("请输入竖直方向的权重:"))
  print(x)
  fun_goTo_center(image,vertical_w=x)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
