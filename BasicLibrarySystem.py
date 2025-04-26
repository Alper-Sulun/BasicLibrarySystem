import tkinter as tk
from tkinter import messagebox,ttk
import time

class MyGUI:

    def __init__(self):
        # Tkinter Arayüzü Oluşturma
        self.root = tk.Tk()

        # Arayüz Başlığı
        self.root.title("Proje")

        # Grid Yapısı
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Arayüz boyutu
        self.root.geometry("600x600")

        # Zaman değişkenleri
        self.startTime = 0
        self.endTime = 0

        # Proje Label
        projeLabel = tk.Label(self.root, text="Programlama Lab-1 Proje", font=("Helvetica", 16))
        projeLabel.grid(row=0,column=0,columnspan=2,sticky="NSEW")

        # Menu Label
        menuLabel = tk.Label(self.root, text=" Choose Function: ")
        menuLabel.grid(row=1 , column=0,sticky="E")

        # Combo Box
        self.combo_box = ttk.Combobox(self.root, values=["Alt Alta Yazdirma", "Orjinal , Ters", "Buyuk A","Ayri Ayri", "Birlestirme", "Kac Unlu"], state="readonly")
        self.combo_box.grid(row=1, column=1, sticky="W")

        # Combobox Default Değeri
        self.combo_box.set("Alt Alta Yazdirma")

        # Metin Giriş Alanı
        textEntryLabel = tk.Label(self.root, text="Enter your text: ")
        textEntryLabel.grid(row=3, column=0,sticky="E")

        self.textEntry = tk.Entry(self.root,width=30)
        self.textEntry.grid(row=3, column=1,pady=10,sticky="NSEW")

        # Frame
        self.buttonFrame = tk.Frame(self.root)

        # Fonksiyon Uygulama Butonu
        applyButton = tk.Button(self.buttonFrame, text="Apply Function",command=self.applyFunction)
        applyButton.pack(side="left")

        # Temizleme Butonu
        deleteButton = tk.Button(self.buttonFrame, text="Delete",command=self.deleteFunction)
        deleteButton.pack(side="left",padx=10)

        self.buttonFrame.grid(row=4,column=1, sticky="NSEW")

        # Metin Çıktı Alanı
        textOutputLabel = tk.Label(self.root, text="Output: ")
        textOutputLabel.grid(row=5, column=0,sticky="E",)

        self.textOutput = tk.Text(self.root,width=50,state="disabled")
        self.textOutput.grid(row=5, column=1,pady=10,sticky="NSEW",padx=2)

        self.startTimer = tk.Button(self.buttonFrame, text="Start Timer",command=self.yaziHizi)
        self.startTimer.pack(side="left",padx=10)

        # Arayüzü çalıştırmaya yarayan döngü
        self.root.mainloop()

    def applyFunction(self):
        self.textOutput.config(state="normal")
        # Comboboxtan seçilen fonksiyonu bulma
        try:
            currentText = self.textEntry.get()
            if currentText == "":
                messagebox.showerror("Error", "Lütfen Metin Giriniz")
            elif currentText.isdigit():
                messagebox.showerror("Error", "Lütfen Sadece Harf Giriniz")
            else:
                currentFunction = self.combo_box.get()
                if currentFunction == "Alt Alta Yazdirma":
                    self.altAltaYazdirma()
                elif currentFunction == "Orjinal , Ters":
                    self.orjinalTers()
                elif currentFunction == "Buyuk A":
                    self.buyukA()
                elif currentFunction == "Ayri Ayri":
                    self.ayriAyri()
                elif currentFunction == "Birlestirme":
                    self.birlestirme()
                elif currentFunction == "Kac Unlu":
                    self.kacUnlu()
                #elif currentFunction == "Yazi Hizi":
                #    self.yaziHizi()
                else:
                    messagebox.showerror("Error", "Invalid Function")
        except:
            messagebox.showerror("Error", "Bir Hata Oluştu")

        #Textbox temizlenmeden başka fonksiyon uygulanınca alttan başlatmak için
        self.textOutput.insert("end","\n")
        self.textOutput.config(state="disabled")

    def deleteFunction(self):
        self.textOutput.config(state="normal")
        self.textEntry.delete(0, "end")
        self.textOutput.delete("1.0", "end")
        self.startTime = 0
        self.endTime = 0

    def altAltaYazdirma(self)->str:
        currentText = self.textEntry.get()
        for i in currentText:
            self.textOutput.insert("end" ,i + "\n")
        self.textOutput.insert("end","Metnin Harfleri Listelendi.\n")

    def orjinalTers(self)->str:
        currentText = self.textEntry.get()
        self.textOutput.insert("end","Cümlenin Orjinali : " + currentText + "\n")
        self.textOutput.insert("end","Cümlenin Tersi : " + currentText[::-1] + "\n")
        self.textOutput.insert("end","Kelime Kelime Tersi alınmış hali: " + " ".join([i[::-1] for i in currentText.split()]) + "\n")

    def buyukA(self)->str:
        currentText = self.textEntry.get()
        for i in currentText:
            if i == "a":
                self.textOutput.insert("end","A")
            else:
                self.textOutput.insert("end",i)

    def ayriAyri(self)->str:
        currentText = self.textEntry.get()
        wordList = currentText.split(sep=" ")
        #Textboxda listeyi gösterirken ['kelime1','kelime2'] şeklinde göstermek için yapılan hile
        self.textOutput.insert("end","[")
        for i in wordList:
            self.textOutput.insert("end","'"+i+"'"+",")
        self.textOutput.insert("end","]")

    def birlestirme(self)->str:
        currentText = self.textEntry.get()
        self.textOutput.insert("end",currentText.replace(" ",""))

    def kacUnlu(self)->str:
        currentText = self.textEntry.get()
        vowel = "aeıiouöüAEIİOUÖÜ"
        count = 0
        for i in currentText:
            if i in vowel:
                count += 1
        self.textOutput.insert("end",currentText + "\n")
        self.textOutput.insert("end","Metindeki Ünlü Harf Sayısı: " + str(count))

    def yaziHizi(self):
        self.textOutput.config(state="normal")
        self.startTime = time.time()
        self.textOutput.insert("end","Zamanlayıcı Başladı. Durdurmak için 'enter'a basınız\n")
        self.root.bind("<Return>",self.keyPressed)        

    def keyPressed(self,event):
        self.endTime = time.time()
        self.textOutput.insert("end","Zamanlayıcı Durdu\n")
        self.textOutput.insert("end","Geçen Süre: " + str(self.endTime - self.startTime) + " saniye\n")
        #self.textOutput.insert("end","words per second: " + str(len(self.textEntry.get().split()) / (self.endTime - self.startTime)) + "\n")
        self.textOutput.insert("end","Letters per second: " + str(len(self.textEntry.get()) / (self.endTime - self.startTime)) + "\n")
        self.startTime = 0
        self.endTime = 0
        self.root.unbind("<Return>")
        self.textOutput.config(state="disabled")

def main():
    MyGUI()

if __name__ == "__main__":
    main()