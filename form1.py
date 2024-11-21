import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Button, Frame
from PIL import Image, ImageTk

# Fungsi untuk memuat gambar dari explorer
def upload_image():
    global img, img_display, img_gray
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img.shape[:2]
    scale = min(400 / width, 400 / height)
    new_size = (int(width * scale), int(height * scale))
    img_resized = cv2.resize(img, new_size)  # Mengubah ukuran gambar agar tidak terlalu besar
    img_display = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)))
    image_label.config(image=img_display, text="Original Image")
    image_label.image = img_display

# Fungsi untuk menghasilkan gambar negatif
def image_negative():
    negative_img = 255 - img_gray
    negative_img_display = ImageTk.PhotoImage(Image.fromarray(negative_img))
    image_label.config(image=negative_img_display, text="Image Negative")
    image_label.image = negative_img_display

# Fungsi untuk melakukan Log Transformation
def log_transformation():
    c = 255 / np.log(1 + np.max(img_gray))
    log_img = c * (np.log(img_gray + 1))
    log_img = np.array(log_img, dtype=np.uint8)
    log_img_display = ImageTk.PhotoImage(Image.fromarray(log_img))
    image_label.config(image=log_img_display, text="Log Transformation")
    image_label.image = log_img_display

# Fungsi untuk melakukan Power-Law Transformations (Gamma Correction)
def power_law_transformation():
    gamma = 2.0  # Anda bisa mengubah nilai gamma sesuai kebutuhan
    power_img = np.array(255 * (img_gray / 255) ** gamma, dtype='uint8')
    power_img_display = ImageTk.PhotoImage(Image.fromarray(power_img))
    image_label.config(image=power_img_display, text="Power-Law Transformation (Gamma Correction)")
    image_label.image = power_img_display

# Fungsi untuk Piecewise-Linear Transformation
def piecewise_linear_transformation():
    r1, s1 = 70, 0
    r2, s2 = 140, 255
    piecewise_img = np.piecewise(img_gray,
                                 [img_gray <= r1, (img_gray > r1) & (img_gray <= r2), img_gray > r2],
                                 [lambda x: (s1 / r1) * x,
                                  lambda x: ((s2 - s1) / (r2 - r1)) * (x - r1) + s1,
                                  lambda x: ((255 - s2) / (255 - r2)) * (x - r2) + s2])
    piecewise_img = np.array(piecewise_img, dtype=np.uint8)
    piecewise_img_display = ImageTk.PhotoImage(Image.fromarray(piecewise_img))
    image_label.config(image=piecewise_img_display, text="Piecewise-Linear Transformation")
    image_label.image = piecewise_img_display

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Digital Image Processing - Form 1")

# Label untuk menampilkan gambar
image_label = Label(root, text="", font=("Helvetica", 16))
image_label.pack()

# Frame untuk menampung tombol agar sejajar
button_frame = Frame(root)
button_frame.pack()

# Tombol untuk mengunggah gambar
upload_button = Button(button_frame, text="Upload Gambar", command=upload_image)
upload_button.grid(row=0, column=0, padx=5, pady=5)

# Tombol untuk Image Negative
negative_button = Button(button_frame, text="Image Negative", command=image_negative)
negative_button.grid(row=0, column=1, padx=5, pady=5)

# Tombol untuk Log Transformations
log_button = Button(button_frame, text="Log Transformations", command=log_transformation)
log_button.grid(row=0, column=2, padx=5, pady=5)

# Tombol untuk Power-Law Transformations
power_law_button = Button(button_frame, text="Power-Law Transformations", command=power_law_transformation)
power_law_button.grid(row=0, column=3, padx=5, pady=5)

# Tombol untuk Piecewise-Linear Transformation Functions
piecewise_button = Button(button_frame, text="Piecewise-Linear Transformations", command=piecewise_linear_transformation)
piecewise_button.grid(row=0, column=4, padx=5, pady=5)

# Menjalankan aplikasi Tkinter
root.mainloop()
