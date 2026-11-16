import tkinter as tk
from PIL import Image, ImageTk
import os

def resize_image(path, target_width, target_height):
    """
    Resize an image to fit within target dimensions while keeping aspect ratio.
    Returns a PhotoImage object for Tkinter.
    """
    try:
        # Open the image
        img = Image.open(path)

        # Calculate aspect ratio preserving size
        img.thumbnail((target_width, target_height), Image.LANCZOS)

        # Convert to Tkinter-compatible PhotoImage
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found: {path}")
    except Exception as e:
        raise RuntimeError(f"Error processing image: {e}")

# --- Tkinter GUI ---
root = tk.Tk()
root.title("Image Resize Example")

# Path to your image
image_path = "./images/grey_dot.png"  # Replace with your image file

if not os.path.exists(image_path):
    print(f"Error: {image_path} does not exist.")
    root.destroy()
else:
    # Resize image to fit within 300x200 pixels
    photo = resize_image(image_path, 10, 10)

    # Display image in a label
    label = tk.Label(root, image=photo)
    label.pack(padx=10, pady=10)
print(photo)
root.mainloop()
