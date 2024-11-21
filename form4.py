import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2

# Global variables
images = [None, None]

# Function to upload and display image
def upload_image(index, panel):
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))  # Make sure it is not too large
        img_tk = ImageTk.PhotoImage(img)
        panel.configure(image=img_tk)
        panel.image = img_tk
        images[index] = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    else:
        messagebox.showerror("Error", "No image selected")

# Function to apply bitwise operation
def apply_operation(op):
    if images[0] is not None and images[1] is not None:
        try:
            h, w = min(images[0].shape[0], images[1].shape[0]), min(images[0].shape[1], images[1].shape[1])
            resized_images = [cv2.resize(img, (w, h)) for img in images]
            result = op(resized_images[0], resized_images[1])
            show_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please upload both images first")

# Function to display result image
def show_result(result_image):
    result_image = Image.fromarray(result_image)
    result_image = result_image.resize((300, 300), Image.LANCZOS)  # Resize to fit within the frame comfortably
    img_tk = ImageTk.PhotoImage(result_image)
    panel_result.configure(image=img_tk)
    panel_result.image = img_tk

# Create main window
root = tk.Tk()
root.title("Digital Image Logic Operation")
root.geometry("800x700")
root.configure(bg="#e6e6e6")

# Frame for uploading images
frame_upload = tk.Frame(root, bg="#e6e6e6")
frame_upload.pack(pady=10)

# Upload buttons
btn_upload_1 = tk.Button(frame_upload, text="Upload Image 1", command=lambda: upload_image(0, panel_image_1), width=20)
btn_upload_1.grid(row=0, column=0, padx=10, pady=10)
btn_upload_2 = tk.Button(frame_upload, text="Upload Image 2", command=lambda: upload_image(1, panel_image_2), width=20)
btn_upload_2.grid(row=0, column=1, padx=10, pady=10)

# Frame for image panels
frame_images = tk.Frame(root, bg="#e6e6e6")
frame_images.pack(pady=10)

# Image display panels without fixed width/height
panel_image_1 = tk.Label(frame_images, bg="#d9d9d9", relief="solid", padx=5, pady=5, borderwidth=2)
panel_image_1.grid(row=0, column=0, padx=20, pady=10)
panel_image_2 = tk.Label(frame_images, bg="#d9d9d9", relief="solid", padx=5, pady=5, borderwidth=2)
panel_image_2.grid(row=0, column=1, padx=20, pady=10)

# Frame for logic operation buttons
frame_operations = tk.Frame(root, bg="#e6e6e6")
frame_operations.pack(pady=10)

# Logic operation buttons
operations = {"AND": cv2.bitwise_and, "OR": cv2.bitwise_or, "XOR": cv2.bitwise_xor}
for name, op in operations.items():
    btn = tk.Button(frame_operations, text=name, command=lambda op=op: apply_operation(op), width=15)
    btn.pack(side="left", padx=15)

# Frame for displaying the result
frame_result = tk.Frame(root, bg="#e6e6e6")
frame_result.pack(pady=10)

# Panel to display the result without fixed width/height
panel_result = tk.Label(frame_result, bg="#d9d9d9", relief="solid", padx=5, pady=5, borderwidth=2)
panel_result.pack(pady=10)

# Run main loop
root.mainloop()
