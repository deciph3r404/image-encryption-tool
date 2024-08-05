import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt_text(text, key):
    return ''.join(chr((ord(char) + key) % 256) for char in text)

def decrypt_text(text, key):
    return ''.join(chr((ord(char) - key) % 256) for char in text)

def load_text_file():
    global loaded_file_path
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                text_display.delete(1.0, tk.END)
                text_display.insert(tk.END, text)
                loaded_file_path = file_path
                status_label.config(text="Text file loaded successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load text file: {e}")
    else:
        messagebox.showinfo("Info", "No file selected")

def encrypt():
    if 'loaded_file_path' in globals():
        key_str = key_entry.get()
        if not key_str.isdigit():
            messagebox.showerror("Error", "Key must be an integer between 0 and 255")
            return
        
        key = int(key_str)
        if not (0 <= key <= 255):
            messagebox.showerror("Error", "Key must be between 0 and 255")
            return
        
        text = text_display.get(1.0, tk.END).rstrip('\n')  # Strip trailing newline characters
        encrypted_text = encrypt_text(text, key)
        
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_path:
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(encrypted_text)
                text_display.delete(1.0, tk.END)
                text_display.insert(tk.END, encrypted_text)
                status_label.config(text=f"Text encrypted and saved as '{save_path}'")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save encrypted text: {e}")
    else:
        messagebox.showinfo("Info", "Please load a text file first")

def decrypt():
    if 'loaded_file_path' in globals():
        key_str = key_entry.get()
        if not key_str.isdigit():
            messagebox.showerror("Error", "Key must be an integer between 0 and 255")
            return
        
        key = int(key_str)
        if not (0 <= key <= 255):
            messagebox.showerror("Error", "Key must be between 0 and 255")
            return
        
        text = text_display.get(1.0, tk.END).rstrip('\n')  # Strip trailing newline characters
        decrypted_text = decrypt_text(text, key)
        
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_path:
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(decrypted_text)
                text_display.delete(1.0, tk.END)
                text_display.insert(tk.END, decrypted_text)
                status_label.config(text=f"Text decrypted and saved as '{save_path}'")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save decrypted text: {e}")
    else:
        messagebox.showinfo("Info", "Please load a text file first")

root = tk.Tk()
root.title("Text Encryption Tool")

load_button = tk.Button(root, text="Load Text File", command=load_text_file)
load_button.pack()

text_display = tk.Text(root, wrap='word')
text_display.pack()

key_label = tk.Label(root, text="Key (0-255):")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
