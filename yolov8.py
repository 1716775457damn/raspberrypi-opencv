# This is the code for yolov8

# 推理检测
# yolo predict model=yolov8n.pt source=4.png

# #训川练自己的数据集
# yolo detect train data=datasets/wheat/my_data.yaml model=yolov8n.yaml pretrained=ultralytics/yolov8n.pt epochs=300 batch=4 1r0=0.01 resume=True

# yolo train data=/home/newbie/txw/yolov8/ultralytics/ultralytics/cfg/datasets/coco.yaml pretrained=/home/newbie/txw/yolov8/yolov8n.pt epochs=300 batch=4 lr0=0.01 resume=True
# 验证模型
# yolo detect val data=datasets/wheat/my_data.yaml
# model=runs/detect/train7/weights/best.pt batch=4

#this code is for mmdetection

# python demo/image_demo.py demo/demo.jpg rtmdet_tiny_8xb32-300e_coco.py --weights rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth --device cpu