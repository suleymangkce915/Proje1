import tkinter as tk
import subprocess

def arabayarisi():
    subprocess.run(["python", "arabayarisi.py"])

def tetris():
    subprocess.run(["python", "tetris.py"])

def yilanoyunu():
    subprocess.run(["python", "yilanoyunu.py"])


pencere = tk.Tk()
pencere.title('Oyunlar')
ekrangenisligi=pencere.winfo_screenwidth()//2-140
ekranyuksekligi=pencere.winfo_screenheight()//2-170

pencere.geometry("280x340+{}+{}".format(ekrangenisligi, ekranyuksekligi))

button1 = tk.Button(pencere, text="Araba Yarışı",font="Courier 14 bold", width=15, justify="center", command=arabayarisi)
button1.place(x=50, y=50)

button2 = tk.Button(pencere, text="Tetris", font="Courier 14 bold", width=15, justify="center", command=tetris)
button2.place(x=50, y=100)

button3 = tk.Button(pencere, text="Yılan Oyunu", font="courier 14 bold", width=15, justify="center", command=yilanoyunu)
button3.place(x=50, y=150)

button4 = tk.Button(pencere, text="Çıkış", font="Courier 14 bold", width=15, justify="center", command=exit)
button4.place(x=50, y=250)

pencere.mainloop()