import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import ctypes


def imageuploader():
    filetypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    try:
        path = filedialog.askopenfilename(filetypes=filetypes)

        if not path: # user canceled
            return

        if not os.path.exists(path): # checks if file exists
            messagebox.showerror("Error", "Could not find file.")
            return

        image = Image.open(path)
        image.thumbnail((400, 400))
        tk_img = ImageTk.PhotoImage(image)
        img_display_label.config(image=tk_img)
        img_display_label.image = tk_img
        file_name_label.config(text=os.path.basename(path))

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file:\n{e}")

ctypes.windll.shcore.SetProcessDpiAwareness(1) # make window look sharp and not blurry
root = tk.Tk()
root.title("Image watermarking")
root.geometry("600x600")
frame = ttk.Frame(root, padding=10)
frame.grid()
heading_label = ttk.Label(frame, text="To imprint a watermark on an image, upload image here.", font=("Arial", 10))
heading_label.grid(column=0, row=0)
upload_btn = ttk.Button(frame, text="Browse files", command=imageuploader)
upload_btn.grid(column=0, row=1)
file_name_label = ttk.Label(frame, text="", font=("Arial", 10))
file_name_label.grid(column=0, row=2)
img_display_label = ttk.Label(frame)
img_display_label.grid(column=0, row=3)
root.mainloop()