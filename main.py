import cv2
import random
#Sanvi face
# Open webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Random mood selection
        mood = random.choice(["😊", "😡", "😢", "😎", "😄"])

        # Display emoji above the face
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, mood, (x, y - 10), font, 1.5, (255, 255, 255), 2)

    cv2.imshow('Mood Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
