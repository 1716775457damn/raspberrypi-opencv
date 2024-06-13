import cv2
from ultralytics import YOLO

# Load the trained YOLOv8 model (adjust the path to your model file)
model = YOLO('box-obb.pt')

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 is the default device ID for the webcam

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLOv8 model on the frame
    results = model(frame)

    # Extract the detections
    detections = results[0].boxes.xyxy.cpu().numpy()  # xyxy format (xmin, ymin, xmax, ymax, confidence, class)

    # Loop over detections and draw bounding boxes
    for det in detections:
        xmin, ymin, xmax, ymax, confidence, class_id = det
        if confidence > 0.5:  # Confidence threshold
            cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
            label = f"{model.names[int(class_id)]}: {confidence:.2f}"
            cv2.putText(frame, label, (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('YOLOv8 Box Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()