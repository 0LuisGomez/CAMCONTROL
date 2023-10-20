import mediapipe as mp
import cv2
import tkinter as tk
from PIL import Image, ImageTk


class CameraInput(tk.Frame):
    def __init__(self, master=None, width=400, height=400):
        super().__init__(master)

        # Create a label to display the camera input
        self.label = tk.Label(self, width=width, height=height)
        self.label.pack()

        # Open the camera
        self.cap = cv2.VideoCapture(2)

        # Create a Mediapipe hand detection object
        self.mp_hands = mp.solutions.hands.Hands()

        # Create a Mediapipe drawing object
        self.mp_drawing = mp.solutions.drawing_utils

        # Schedule the function to update the label with the current camera input
        self.update_label()

    def update_label(self):
        # Read a frame from the camera
        ret, frame = self.cap.read()

        # Detect hands in the frame using Mediapipe
        results = self.mp_hands.process(frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw the hand landmarks on the frame
                self.mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS
                )

        # Convert the frame to a PIL Image
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        image = Image.fromarray(image)

        # Resize the image to fit in the label
        size = (self.label.winfo_width(), self.label.winfo_height())
        image = image.resize(size)

        # Convert the image to a PhotoImage and set it as the label's image
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo

        # Schedule the function to run again after 10 milliseconds
        self.after(10, self.update_label)
