import os
import platform
import random
import tkinter as tk
from tkinter import messagebox

# Secret fruit list
DAFTAR_BUAH = ["apple", "mango", "banana", "watermelon", "grape", "durian"]
secret_fruit = random.choice(DAFTAR_BUAH)


def shutdown_pc():
    current_os = platform.system()
    if current_os == "Windows":
        os.system("shutdown /s /t 5")
    elif current_os == "Linux" or current_os == "Darwin":
        os.system("sudo shutdown now")


def cek_tebakan():
    global secret_fruit
    tebakan = entry_tebakan.get().strip().lower()

    if not tebakan:
        messagebox.showwarning("Warning", "Fruit name cannot be empty!")
        return

    if tebakan == secret_fruit:
        messagebox.showinfo(
            "Congratulations!",
            f"CORRECT! ({secret_fruit}). Your PC has survived the doom!",
        )
        root.destroy()
    else:
        messagebox.showerror(
            "Game Over!",
            f"WRONG! The correct fruit was '{secret_fruit}'. Your PC will CRASH IN 5 MINUTES",
        )
        shutdown_pc()
        root.destroy()


# Create Main GUI Window
root = tk.Tk()
root.title("Fruit of Doom - Desktop Edition")
root.geometry("450x300")
root.config(bg="#12141c")

# Title Label
label_judul = tk.Label(
    root,
    text="🍎 FRUIT OF DOOM 🍌",
    font=("Arial", 18, "bold"),
    fg="#ff3366",
    bg="#12141c",
)
label_judul.pack(pady=15)

# Instructions Label
petunjuk_text = (
    "Available Fruits:\n[apple, mango, banana, watermelon, grape, durian]\n\n⚠️"
    " WRONG GUESS = PC SHUTDOWN!"
)
label_info = tk.Label(
    root,
    text=petunjuk_text,
    font=("Arial", 11),
    fg="#e0e0e0",
    bg="#12141c",
    justify="center",
)
label_info.pack(pady=5)

# Text Input Box
entry_tebakan = tk.Entry(
    root, font=("Arial", 14), justify="center", bd=2, relief="solid"
)
entry_tebakan.pack(pady=15, ipadx=10, ipady=5)

# Submit Button
btn_tebak = tk.Button(
    root,
    text="GUESS NOW",
    font=("Arial", 12, "bold"),
    bg="#ff3366",
    fg="white",
    activebackground="#ff194d",
    activeforeground="white",
    padx=10,
    pady=5,
    command=cek_tebakan,
)
btn_tebak.pack(pady=10)

# Run application
root.mainloop()