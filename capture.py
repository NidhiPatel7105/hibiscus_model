import cv2
import os

# Set save path
save_dir = "static/uploads"
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, "captured_image.jpg")

# Start webcam capture
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Image (Press SPACE to Save)", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 32:  # SPACE key
        cv2.imwrite(save_path, frame)
        print(f"Image saved to {save_path}")
        break
    elif key == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
