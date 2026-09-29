import cv2
from ultralytics import YOLO

# 1. Load your newly trained AI model file (must be in the same folder)
try:
    model = YOLO('best.pt')
except Exception as e:
    print("Error: Could not find 'best.pt' in this folder. Make sure to download it from Colab!")
    exit()

# 2. Start your live camera stream (0 is your default built-in or USB webcam)
cap = cv2.VideoCapture(0)

print("Starting Car Dashboard Obstacle Detection System...")
print("Press 'q' on your keyboard to close the window.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Error: Camera feed interrupted.")
        break

    # 3. Feed the camera frame directly into your custom AI model
    results = model(frame, verbose=False)

    # 4. Extract data to evaluate obstacle location, shape, and size
    for result in results:
        for box in result.boxes:
            # Get bounding box coordinates: top-left (x1, y1), bottom-right (x2, y2)
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # Calculate total pixel area to judge obstacle size/proximity
            width = x2 - x1
            height = y2 - y1
            area = width * height
            
            # Fetch the specific classification name assigned by the AI
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            confidence = float(box.conf[0]) * 100

            # Obstacle avoidance alert threshold logic
            if area > 60000:  # If an obstacle occupies a massive portion of the frame
                alert_status = "CRITICAL HAZARD - EVADE!"
                color = (0, 0, 255)  # Bright Red
            else:
                alert_status = "Tracking Object"
                color = (0, 255, 255)  # Amber Yellow

            # 5. Render boxes and notifications dynamically onto the camera feed
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} ({confidence:.1f}%) - {alert_status}", 
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # 6. Open a window on your desktop showing the live dashcam visualization
    cv2.imshow('Car Dashboard Camera System', frame)

    # Press the 'q' key to clean up and close the program safely
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean exit protocols
cap.release()
cv2.destroyAllWindows()
