import face_recognition
import cv2
import os

# Load the known image from the images/ folder
known_image_path = os.path.join("images", "yash.jpg")
known_image = face_recognition.load_image_file(known_image_path)
known_encoding = face_recognition.face_encodings(known_image)[0]

# Start the webcam
video_capture = cv2.VideoCapture(0)

print("🔍 Scanning for face...")

while True:
    ret, frame = video_capture.read()

    # Resize frame for faster processing (optional)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR (OpenCV) to RGB (face_recognition)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Get face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        # Compare with the known encoding
        match = face_recognition.compare_faces([known_encoding], face_encoding)

        if match[0]:
            print("✅ Access Granted")
        else:
            print("❌ Access Denied")

    # Display the video feed
    cv2.imshow('IGRIS Face Authentication', frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()

