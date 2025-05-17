
import datetime
import tkinter as tk
import subprocess

x = datetime.datetime.now()
x_str = x.strftime("%d.%m.%Y")


def havadurumu():
    subprocess.run(["python", "havadurumu.py"])

def takvim():
    subprocess.run(["python", "takvim.py"])

def hesapmakinasi():
    subprocess.run(["python", "hesapmakinasi.py"])

def oyunlar():
    subprocess.run(["python", "oyunlar.py"])
 
pencere = tk.Tk()
pencere.title('Ana Ekran')
ekrangenisligi=pencere.winfo_screenwidth()//2-175
ekranyuksekligi=pencere.winfo_screenheight()//2-275

pencere.geometry("350x550+{}+{}".format(ekrangenisligi, ekranyuksekligi))

button0 = tk.Label(pencere, text=x_str, font="Courier 8 bold", width=30, justify="center")
button0.place(x=70, y=20)

button1 = tk.Button(pencere, text="Hava Durumu", font="Courier 16 bold", width=15, justify="center", command=havadurumu)
button1.place(x=70, y=100)

button2 = tk.Button(pencere, text="Takvim", font="Courier 16 bold", width=8, justify="center", command=takvim)
button2.place(x=120, y=160)

button3 = tk.Button(pencere, text="Hesap Makinesi", font="courier 16 bold", width=15, justify="center", command=hesapmakinasi)
button3.place(x=80, y=220)

button4 = tk.Button(pencere, text="Oyunlar", font="Courier 16 bold", width=10, justify="center", command=oyunlar)
button4.place(x=120, y=280)

button5 = tk.Button(pencere, text="Çıkış", font="Courier 16 bold", justify="center", command=exit)
button5.place(x=125, y=450)


pencere.mainloop()  
