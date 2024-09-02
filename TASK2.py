import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEncryptor:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Manipulation for Image Encryption")

        # Create input section
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill="x")
        self.image_label = tk.Label(self.input_frame, text="Select Image:")
        self.image_label.pack(side="left")
        self.image_entry = tk.Entry(self.input_frame, width=40)
        self.image_entry.pack(side="left")
        self.browse_button = tk.Button(self.input_frame, text="Browse", command=self.browse_image)
        self.browse_button.pack(side="left")

        # Create encrypt section
        self.encrypt_frame = tk.Frame(self.root)
        self.encrypt_frame.pack(fill="x")
        self.key_label = tk.Label(self.encrypt_frame, text="Enter Key:")
        self.key_label.pack(side="left")
        self.key_entry = tk.Entry(self.encrypt_frame, width=10)
        self.key_entry.pack(side="left")
        self.encrypt_button = tk.Button(self.encrypt_frame, text="Encrypt", command=self.encrypt_image)
        self.encrypt_button.pack(side="left")

        # Create decrypt section
        self.decrypt_frame = tk.Frame(self.root)
        self.decrypt_frame.pack(fill="x")
        self.decrypt_button = tk.Button(self.decrypt_frame, text="Decrypt", command=self.decrypt_image)
        self.decrypt_button.pack(side="left")

        # Create image display section
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(fill="both", expand=True)
        self.display_image_label = tk.Label(self.display_frame)
        self.display_image_label.pack(fill="both", expand=True)

    def browse_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".png .jpg .jpeg")])
        self.image_entry.delete(0, tk.END)
        self.image_entry.insert(0, image_path)
        self.display_image(image_path)

    def display_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.display_image_label.config(image=photo)
        self.display_image_label.image = photo

    def encrypt_image(self):
        image_path = self.image_entry.get()
        key = int(self.key_entry.get())
        image = Image.open(image_path)
        pixels = list(image.getdata())

        # Check if the image has an alpha channel
        if image.mode == 'RGBA':
            encrypted_pixels = [(r ^ key, g ^ key, b ^ key, a) for r, g, b, a in pixels]
        else:
            encrypted_pixels = [(r ^ key, g ^ key, b ^ key) for r, g, b in pixels]

        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixels)
        encrypted_image.save("encrypted_image.png")

        self.image_entry.delete(0, tk.END)
        self.image_entry.insert(0, "encrypted_image.png")
        self.display_image("encrypted_image.png")

    def decrypt_image(self):
        image_path = self.image_entry.get()
        key = int(self.key_entry.get())
        image = Image.open(image_path)
        pixels = list(image.getdata())

        # Check if the image has an alpha channel
        if image.mode == 'RGBA':
            decrypted_pixels = [(r ^ key, g ^ key, b ^ key, a) for r, g, b, a in pixels]
        else:
            decrypted_pixels = [(r ^ key, g ^ key, b ^ key) for r, g, b in pixels]

        decrypted_image = Image.new(image.mode, image.size)
        decrypted_image.putdata(decrypted_pixels)
        decrypted_image.save("decrypted_image.png")

        self.image_entry.delete(0, tk.END)
        self.image_entry.insert(0, "decrypted_image.png")
        self.display_image("decrypted_image.png")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptor(root)
    root.mainloop()
