import face_recognition
import cv2
import numpy as np
import os

def authenticate_user():
    print("🧠 Initializing face recognition...")

    # Correct path to image
    script_dir = os.path.dirname(os.path.abspath(__file__))
    known_image_path = os.path.join(script_dir, "images", "authorized_user.jpg")

    if not os.path.exists(known_image_path):
        print(f"❌ Authorized user image not found at: {known_image_path}")
        return

    known_image = face_recognition.load_image_file(known_image_path)
    known_encodings = face_recognition.face_encodings(known_image)

    if not known_encodings:
        print("❌ Failed to find a face in the authorized image.")
        return

    known_encoding = known_encodings[0]

    # Start webcam
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("❌ Could not access the camera.")
        return

    print("📷 Camera started. Press 'Q' to quit.\n🔍 Looking for a match...")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("❌ Failed to read from camera.")
            break

        # Resize and convert for processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            match = face_recognition.compare_faces([known_encoding], face_encoding)[0]
            distance = face_recognition.face_distance([known_encoding], face_encoding)[0]

            if match:
                print(f"✅ Authorized user recognized! Distance: {distance:.2f}")
                video_capture.release()
                cv2.destroyAllWindows()
                return True
            else:
                print(f"🔒 Face not authorized. Distance: {distance:.2f}")

        cv2.imshow('Authentication', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("❌ Authentication cancelled.")
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return False

if __name__ == "__main__":
    authenticate_user()
