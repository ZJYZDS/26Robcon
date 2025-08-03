import cv2
import numpy as np



#____
def fun_goTo_center(image,step=10,start_x=100,strat_y=300):
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
    aim_x=shape[1]//2
    aim_y=shape[0]//2

    step_x=abs(aim_x-start_x)//step
    step_y=abs(aim_y-strat_y)//step

    degree_x=0;degree_y=0

    temp_x=start_x;temp_y=strat_y
    trajectory=[(temp_x,temp_y)]

    total_step=step_x+step_y
    for _ in range(0,total_step,1):
        if (degree_x/step_x)<=(degree_y/step_y):
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
  fun_goTo_center(image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
