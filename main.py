import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import ctypes

image = None
def imageuploader():
    global image
    filetypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    try:
        path = filedialog.askopenfilename(filetypes=filetypes)

        if not path: # user canceled
            return

        if not os.path.exists(path): # checks if file exists
            messagebox.showerror("Error", "Could not find file.")
            return

        image = Image.open(path)
        w, h = image.size
        new_h = 250
        new_w = int(w * new_h / h)
        image = image.resize((new_w, new_h))
        tk_img = ImageTk.PhotoImage(image)
        img_display_label.config(image=tk_img)
        img_display_label.image = tk_img
        file_name_label.config(text=os.path.basename(path))

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file:\n{e}")

def add_watermark():
    global image
    if not image:
        messagebox.showerror("Error", "No image was selected.")
    else:
        draw = ImageDraw.Draw(image)
        watermark_text = "James' work"
        w, h = image.size
        x, y = int(w/2), int(h/2)
        if x > y:
            font_size = y
        else:
            font_size = x
        position = (0, 0)
        draw.text(position, watermark_text, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", int(font_size/6)))
        tk_img = ImageTk.PhotoImage(image)
        img_display_label.config(image=tk_img)
        img_display_label.image = tk_img

def save_image():
    global image
    if not image:
        messagebox.showerror("Error", "No image was selected.")
    else:
        save_img = filedialog.asksaveasfilename(defaultextension=".jpg")
        image.save(save_img)
        messagebox.showinfo("Success", "Image was created successfully.")

ctypes.windll.shcore.SetProcessDpiAwareness(1) # make window look sharp and not blurry
root = tk.Tk()
root.title("Image watermarking")
root.geometry("600x600")
heading_label = ttk.Label(root, text="To imprint a watermark on an image, upload image here.", font=("Arial", 10))
heading_label.grid(column=0, row=0, columnspan=3)
upload_btn = ttk.Button(root, text="Browse files", command=imageuploader, width=25)
upload_btn.grid(column=1, row=1)
file_name_label = ttk.Label(root, text="", font=("Arial", 10))
file_name_label.grid(column=1, row=2)
img_display_label = ttk.Label(root)
img_display_label.grid(column=1, row=3)
add_water_btn = ttk.Button(root, text="Add watermark", command=add_watermark, width=25)
add_water_btn.grid(column=1, row=4)
save_btn = ttk.Button(root, text="Save", command=save_image, width=25)
save_btn.grid(column=1, row=5)
root.mainloop()