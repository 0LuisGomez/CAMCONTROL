import tkinter as tk
from cameramodule import CameraInput

# Create a window
window = tk.Tk()
window.title("Camera Input")

# Create a CameraInput widget and pack it into the window
camera_input = CameraInput(window)
camera_input.pack()

# Start the main loop
window.mainloop()
