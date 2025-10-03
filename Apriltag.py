import cv2
import pupil_apriltags as apriltag
import numpy as np
import time


#0.定义保存视频存放路径和文件名
save_video_name=r"D:\Python_pro\Open_CV\save_videos\apriltag_video.avi"
fourcc = cv2.VideoWriter.fourcc(*'XVID')
out = cv2.VideoWriter(save_video_name,fourcc,5,(640,480))

#1.初始化摄像头
cap= cv2.VideoCapture(0)
# 检查摄像头是否成功打开
if not cap.isOpened():
    print("摄像头无法打开！！！")
    exit()

# 2. 初始化Apriltag检测器
detector=apriltag.Detector()


# 3. 循环捕获并识别Apriltag
key=True
while(key):
    ret , frame =cap.read()
    time.sleep(0.1)#设置帧率
    # 若读取失败，退出循环
    if not ret:
        print("无法获取视频帧，程序退出")
        break

    # 4. 图像预处理：Apriltag识别需灰度图，将彩色帧转为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. 检测Apriltag，返回识别结果列表
    results = detector.detect(gray)

    # 6. 处理识别结果：在画面上绘制标签轮廓和信息
    for r in results:
        #绘制标签轮廓
        corners = np.array(r.corners, dtype=int)

        #cv2.drawContours(frame,[corners],color=[0,255,0],thickness=2)

        cv2.polylines(frame,[corners],isClosed=True, color=(0,0,255), thickness=2)

        #绘制标签信息
       # text=r.tag_family+"--"+r.tag_id
       # print(type(r.tag_family),type(r.tag_id))
        text=" id== "+str(r.tag_id)
        center=r.center

        #cv2.circle(frame, center, radius=1, color=[36, 28, 237], thickness=-1)
        cv2.putText(frame,text,org=(int(center[0]-6),int(center[1]-2)),fontFace=cv2.QT_FONT_BLACK,fontScale=1,color=[0,0,255])



        #---------------将视频保存----------------------
        out.write(frame)


    # 7. 显示处理后的画面
    cv2.imshow("Apriltag Recognition", frame)

    # 8. 退出程序
    if cv2.waitKey(1) & 0xff==ord('q') :
       key=False


# 9. 释放摄像头与写入资源并关闭所有窗口

cap.release()
out.release()
cv2.destroyAllWindows()




