import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Button, Frame
from PIL import Image, ImageTk


def upload_image():
    global img, img_display, img_gray
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img.shape[:2]
    scale = min(400 / width, 400 / height)
    new_size = (int(width * scale), int(height * scale))
    img_resized = cv2.resize(img, new_size)
    img_display = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)))
    image_label.config(image=img_display, text="Original Image")
    image_label.image = img_display


def bit_plane_slicing():
    bit_planes = []
    for i in range(8):
        bit_plane = (img_gray & (1 << i)) >> i
        bit_plane = bit_plane * 255
        bit_planes.append(bit_plane)

    bit_plane_img = np.hstack(bit_planes)  # Menggabungkan semua bit planes secara horizontal
    bit_plane_img_display = ImageTk.PhotoImage(Image.fromarray(bit_plane_img))
    image_label.config(image=bit_plane_img_display, text="Bit-Plane Slicing")
    image_label.image = bit_plane_img_display

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Digital Image Processing - Form 2")

# Label untuk menampilkan gambar
image_label = Label(root, text="", font=("Helvetica", 16))
image_label.pack()

# Frame untuk menampung tombol agar sejajar
button_frame = Frame(root)
button_frame.pack()

# Tombol untuk mengunggah gambar
upload_button = Button(button_frame, text="Upload Image", command=upload_image)
upload_button.grid(row=0, column=0, padx=5, pady=5)

# Tombol untuk Bit-Plane Slicing
bit_plane_button = Button(button_frame, text="Bit-Plane Slicing", command=bit_plane_slicing)
bit_plane_button.grid(row=0, column=1, padx=5, pady=5)

# Menjalankan aplikasi Tkinter
root.mainloop()
