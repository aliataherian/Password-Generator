import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())  # Get password length
        include_uppercase = uppercase_var.get()
        include_lowercase = lowercase_var.get()
        include_digits = digits_var.get()
        include_special = special_var.get()

        # Validation
        if length < 1:
            raise ValueError("Password length must be at least 1.")

        # Character selection
        characters = ""
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        if not characters:
            raise ValueError("Please select at least one option.")

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)  # Clear previous password
        result_entry.insert(0, password)  # Display new password
        
        # Highlight text for copying
        result_entry.select_range(0, tk.END)
        result_entry.icursor(tk.END)  # Move cursor to the end of the text

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x450")
root.configure(bg="#f5f5f5")  # Background color

# Main title
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Input frame
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(pady=10, fill="x", padx=20)

length_label = ttk.Label(input_frame, text="Password Length:", font=("Helvetica", 12))
length_label.grid(row=0, column=0, sticky="w", pady=5)

length_entry = ttk.Entry(input_frame, width=10, font=("Helvetica", 12))
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Checkboxes
options_frame = ttk.LabelFrame(root, text="Password Settings", padding="10")
options_frame.pack(pady=10, fill="x", padx=20)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)

ttk.Checkbutton(options_frame, text="Include lowercase letters (abcdef)", variable=lowercase_var).pack(anchor="w")
ttk.Checkbutton(options_frame, text="Include uppercase letters (ABCDEF)", variable=uppercase_var).pack(anchor="w")
ttk.Checkbutton(options_frame, text="Include digits (12345)", variable=digits_var).pack(anchor="w")
ttk.Checkbutton(options_frame, text="Include special characters (%$#@)", variable=special_var).pack(anchor="w")

# Generate password button
button_frame = ttk.Frame(root, padding="10")
button_frame.pack(pady=10)

generate_button = ttk.Button(button_frame, text="Generate Password", command=generate_password)
generate_button.pack()

# Display result in Entry
result_frame = ttk.LabelFrame(root, text="Generated Password", padding="10")
result_frame.pack(pady=10, fill="x", padx=20)

result_entry = ttk.Entry(result_frame, font=("Helvetica", 14), justify="center", state="normal")
result_entry.pack(fill="x", padx=10, pady=5)

# Custom styles
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)

# Run the application
root.mainloop()
