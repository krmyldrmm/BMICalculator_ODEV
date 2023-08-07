from tkinter import *

window = Tk()
window.title("Vücut Kitle İndeksi Hesaplayıcı")
window.minsize(width=250, height=300)
window.config(pady=30)

# WEIGHT
weight_label = Label(text="Kilonuzu giriniz (kg).", pady=5)
weight_label.pack()

weight_entry = Entry()
weight_entry.pack()

# HEIGHT
height_label = Label(text="Boyunuzu giriniz (cm).", pady=5)
height_label.pack()

height_entry = Entry()
height_entry.pack()

# CALCULATE

def bmi_calculate():
    if weight_entry.get() == "" or height_entry.get() == "":
        result_label.config(text="Boy ya da kilo boş bırakılamaz..")
    else:
        try:
            weight = weight_entry.get()
            height = height_entry.get()
            result = round(int(weight) / (int(height) / 100) ** 2, 1)
        except ZeroDivisionError:
            result_label.config(text="Boy '0' olamaz")
        except ValueError:
            result_label.config(text="Geçerli bir değer giriniz.")
        else:
            if result < 15:
                result_label.config(text=f"Vücut Kitle İndeksin = {result} ve çok ciddi derecede düşük kilolusun.")
            elif result >= 15 and result <= 16:
                result_label.config(text=f"Vücut Kitle İndeksin = {result} ve ciddi derecede düşük kilolusun.")
            elif result >= 16 and result <= 18.5:
                result_label.config(text=f"Vücut Kitle İndeksin = {result} ve düşük kilolusun.")
            elif result >= 18.5 and result <= 25:
                result_label.config(text=f"Vücut Kitle İndeksin = {result} ve normal (sağlıklı) kilolusun.")
            elif result >= 25 and result <= 30:
                result_label.config(text=f"Vücut Kitle İndeksin = {result} ve fazla kilolusun.")
            elif result >= 30 and result <= 35:
                result_label.config(text=f"Vücut Kitle İndeksin = {result} ve 1. dereceden (hafif) obezsin.")
            elif result >= 35 and result <= 40:
                result_label.config(text=f"Vücut Kitle İndeksin = {result} ve 2. dereceden (ciddi) obezsin.")
            elif result > 40:
                result_label.config(text=f"Vücut Kitle İndeksin = {result} ve 3. dereceden (çok ciddi) obezsin.")
            else:
                result_label.config(text="Bir hata meydana geldi.")

    # result_label.config(text=f"Kilon = {weight}, boyun = {height}")
    result_label.pack()

calculate_button = Button(text="Hesapla", command=bmi_calculate)
calculate_button.pack()

# INVISIBLE RESULT LABEL
result_label = Label(text="")
result_label.pack_forget()

mainloop()
