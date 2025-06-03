#
import datetime as ts
import tkinter as tk
import subprocess

x = ts.datetime.now()
x_str = x.strftime("%H:%M \n %d.%m.%Y")


def takvim():
    subprocess.run(["python3", "takvim.py"])

def hesapmakinasi():
    subprocess.run(["python3", "hesapmakinasi.py"])

def oyunlar():
    subprocess.run(["python3", "oyunlar.py"])
 
pencere = tk.Tk()
pencere.title('Ana Ekran')
ekrangenisligi=pencere.winfo_screenwidth()//2-175
ekranyuksekligi=pencere.winfo_screenheight()//2-275

pencere.geometry("350x550+{}+{}".format(ekrangenisligi, ekranyuksekligi))

button1 = tk.Label(pencere, text=x_str, font="Courier 12 bold", width=30, justify="center")
button1.place(x=30, y=20)

button2 = tk.Button(pencere, text="Takvim", font="Courier 16 bold", width=8, justify="center", command=takvim)
button2.place(x=120, y=160)

button3 = tk.Button(pencere, text="Hesap Makinesi", font="courier 16 bold", width=15, justify="center", command=hesapmakinasi)
button3.place(x=80, y=220)

button4 = tk.Button(pencere, text="Oyunlar", font="Courier 16 bold", width=10, justify="center", command=oyunlar)
button4.place(x=120, y=280)

button5 = tk.Button(pencere, text="Çıkış", font="Courier 16 bold", justify="center", command=exit)
button5.place(x=125, y=450)


pencere.mainloop()  
