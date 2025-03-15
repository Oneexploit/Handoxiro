# Hand Gesture Mouse Control

This project uses MediaPipe and OpenCV to control the mouse cursor using hand gestures in real-time. The program tracks the positions of the thumb and index finger to simulate mouse movements and clicks. It allows for mouse pointer movement and left-clicking based on hand gestures, making it a gesture-based alternative to traditional mouse usage.

## Features
- **Hand Gesture Recognition:** Uses MediaPipe to detect hand landmarks.
- **Mouse Control:** Move the mouse pointer with the index finger and perform left-clicking by pinching the thumb and index finger.
- **Dragging:** Hold the mouse button to simulate dragging when the thumb and index fingers are close together.
- **Real-time Feedback:** Displays hand landmarks on the webcam feed for visualization.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- pyautogui
- pynput
- numpy

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/hand-gesture-mouse-control.git
cd hand-gesture-mouse-control
pip3 install requirements.txt
```
```run
python hand_gesture_mouse_control.py
```
