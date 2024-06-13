# 检测图像
# 引入opencv
import cv2

# 引入YOLO模型
from ultralytics import YOLO

# 打开图像
img_path = "./xiyouji.jpeg"

# 打开图像
img = cv2.imread(filename=img_path)

# 加载模型
model = YOLO(model="yolov8n.pt")

# 正向推理
res = model(img)

# 绘制推理结果
annotated_img = res[0].plot()

# 显示图像
cv2.imshow(winname="YOLOV8", mat=annotated_img)

# 等待时间
cv2.waitKey(delay=10000)

# 绘制推理结果
cv2.imwrite(filename="jieguo.jpeg", img=annotated_img)


# 检测视频
import cv2

from ultralytics import YOLO

# 加载模型
model = YOLO(model="yolov8x.pt")

# 视频文件
video_path = "nanwangjinxiao.mp4"

# 打开视频
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
	# 获取图像
	res, frame = cap.read()
	# 如果读取成功
	if res:
		# 正向推理
		results = model(frame)

		# 绘制结果
		annotated_frame = results[0].plot()

		# 显示图像
		cv2.imshow(winname="YOLOV8", mat=annotated_frame)

		# 按ESC退出
		if cv2.waitKey(1) == 27:
			break

	else:
		break

# 释放链接
cap.release()
# 销毁所有窗口
cv2.destroyAllWindows()


# 实时检测
import cv2

from ultralytics import YOLO

# 加载模型
model = YOLO(model="yolov8n.pt")

# 摄像头编号
camera_no = 0

# 打开摄像头
cap = cv2.VideoCapture(camera_no)

while cap.isOpened():
	# 获取图像
	res, frame = cap.read()
	# 如果读取成功
	if res:
		# 正向推理
		results = model(frame)

		# 绘制结果
		annotated_frame = results[0].plot()

		# 显示图像
		cv2.imshow(winname="YOLOV8", mat=annotated_frame)

		# 按ESC退出
		if cv2.waitKey(1) == 27:
			break

	else:
		break

# 释放链接
cap.release()
# 销毁所有窗口
cv2.destroyAllWindows()