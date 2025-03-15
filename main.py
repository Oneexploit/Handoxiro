import os
import cv2
import mediapipe as mp
import numpy as np
import pyautogui
from pynput.mouse import Button, Controller

# Suppress TensorFlow Lite info messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Initialize mouse controller
mouse = Controller()

# Start video capture
cap = cv2.VideoCapture(0)

# Define screen size (adjust accordingly)
screen_width, screen_height = pyautogui.size()

# Variables to track dragging state
dragging = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get hand landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the frame
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the positions of the thumb and index finger
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Calculate the distance between the thumb and index finger (to simulate "clicking")
            thumb_position = np.array([thumb_tip.x, thumb_tip.y])
            index_position = np.array([index_tip.x, index_tip.y])
            middle_position = np.array([middle_tip.x, middle_tip.y])

            distance_thumb_index = np.linalg.norm(thumb_position - index_position)
            distance_thumb_middle = np.linalg.norm(thumb_position - middle_position)

            # If the thumb and index finger are close, simulate a click (start dragging)
            if distance_thumb_index < 0.05:
                if not dragging:
                    mouse.press(Button.left)  # Start dragging
                    dragging = True
                    print("Start dragging")

            else:
                if dragging:
                    mouse.release(Button.left)  # Release the mouse button to drop the file
                    dragging = False
                    print("Drop file")

            # If the hand is fully open, move the mouse based on the index finger position
            if distance_thumb_middle > 0.1:
                mouse_x = int(index_tip.x * screen_width)
                mouse_y = int(index_tip.y * screen_height)
                mouse.position = (mouse_x, mouse_y)

    # Show the frame with hand landmarks
    cv2.imshow('onexploit', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
