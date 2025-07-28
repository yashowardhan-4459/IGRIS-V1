import cv2
import os

def save_face():
    # Ensure the folder exists
    os.makedirs("face_data", exist_ok=True)

    # Start webcam
    cam = cv2.VideoCapture(0)
    print("📸 Capturing image. Press 's' to save, 'q' to quit.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        cv2.imshow("Capture Face", frame)
        k = cv2.waitKey(1)

        if k % 256 == ord('s'):
            # Save image
            img_path = "face_data/authorized_user.jpg"
            cv2.imwrite(img_path, frame)
            print(f"✅ Image saved at {img_path}")
            break
        elif k % 256 == ord('q'):
            print("❌ Quit without saving.")
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    save_face()
