import tkinter as tk
import calendar
from tkinter import ttk

def show_calendar():
    month = int(month_var.get())
    year = int(year_var.get())
    cal_text = calendar.month(year, month)
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, cal_text)


root = tk.Tk()
root.title("Takvim Uygulaması")


tk.Label(root, text="Yıl:").grid(row=0, column=0)
year_var = tk.StringVar()
year_entry = ttk.Entry(root, textvariable=year_var)
year_entry.grid(row=0, column=1)

tk.Label(root, text="Ay:").grid(row=1, column=0)
month_var = tk.StringVar()
month_entry = ttk.Entry(root, textvariable=month_var)
month_entry.grid(row=1, column=1)


show_btn = ttk.Button(root, text="Takvimi Göster", command=show_calendar)
show_btn.grid(row=2, column=0, columnspan=2, pady=10)


text_box = tk.Text(root, width=20, height=8, font=("Courier", 12))
text_box.grid(row=3, column=0, columnspan=2)


root.mainloop()
