import tkinter as tk
from tkinter import ttk

def search_devices():
    for row in table.get_children():
        table.delete(row)

    devices = [
        ("Galaxy A34", "100 متر", "روشن"),
        ("Redmi Note 12", "75 متر", "خاموش"),
        ("iPhone 13", "50 متر", "روشن"),
        ("Samsung S23", "120 متر", "روشن"),
    ]

    for device in devices:
        table.insert("", tk.END, values=device)

root = tk.Tk()
root.title("سیستم جستجوی دستگاه‌های اطراف")
root.geometry("700x400")

title = tk.Label(
    root,
    text="جستجوی دستگاه‌های اطراف",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

btn = tk.Button(
    root,
    text="جستجو",
    font=("Arial", 12),
    command=search_devices
)
btn.pack(pady=10)

columns = ("نام دستگاه", "فاصله", "وضعیت اینترنت")

table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=200, anchor="center")

table.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
