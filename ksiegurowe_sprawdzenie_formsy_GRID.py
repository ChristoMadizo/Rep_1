#lst=[5,3,564,786,768,45,6577,452,5687,768,57,788,77876]


#lst=lst.replace("\r","").split("\n") #przemienia dane wklejone z excela na listę
#lst=[int(i) for i in lst if i!=""] #konwertuje elementy listy z tekstu na liczby


#suma=1784

#print(float('5.5')*5)

from itertools import chain, combinations
def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

def generuj(): #pobiera tekst z kontrolki, gdzie wklejam liczby z excela
    lst=[]
    lst=txt.get('1.0', 'end') #pobiera tekst z kontrolki
    lst=lst.replace("\r","").split("\n") #przemienia dane wklejone z excela na listę
    lst=[i.replace(",",".") for i in lst]  #zamienia przecinki w liczbach na kropki

    lst=[float(i) for i in lst if i!=""] #konwertuje elementy listy z tekstu na liczby     #*100
    suma=entry1.get().replace(",",".") #pobiera wartość sumy z entry1    #*100

    #print("wciśnięto przycisk")
    ostateczna_lista = []
    for subset in all_subsets(lst): #w tym miejscu wywyłuje funkcję all_subsets() zdefiniowaną wyżej
        #print(str(subset) + " i jego suma: " + str(sum(subset)) + " i suma do sprawdzenia: " + str(suma))
        #test=sum(subset)-suma
        #print(test)
        if sum(subset) == float(suma):   #to wersja superdokładna
        #if abs(sum(subset) == float(suma))<10: #to wersja dopuszczająca różnicę do 10 PLN/EUR - nie działa, bo zwraca wszytkie rekordy
            print(float(suma))
            print(sum(subset))
            ostateczna_lista.append(subset)
    print("ostateczna lista: " + str(ostateczna_lista))
    #txt.delete('1.0',tk.END) #czyści zawartość widgetu
    txt_wynik.insert(tk.INSERT,ostateczna_lista)

def on_ok(event=None):
    win1.destroy()

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
win1 = tk.Tk()
win1.title("Księgowy liczyciel")
win1.geometry('700x500')

content = ttk.Frame(win1,borderwidth=5, relief="ridge") #tworzy główną ramkę
content.grid(column=0,row=0) #umieszcza główną ramkę w oknie
lbl=tk.Label(content, text="Wklej liczbę:",bd=10,bg="light green",relief=tk.RAISED)
lbl.grid(column=0,row=0,columnspan=1,rowspan=1,padx=5,pady=5,sticky=tk.EW)
txt = scrolledtext.ScrolledText(content,width=10,height=20,bd=10)
txt.grid(column=0,row=1,rowspan=15,columnspan=1,padx=5)
lbl2=tk.Label(content, text="Wklej sumę:",bd=10,bg="light blue",relief=tk.RAISED)
lbl2.grid(column=1,row=0,columnspan=1,rowspan=1,padx=5,pady=5,sticky=tk.EW)
entry1 = tk.Entry(content,width=20,bd=10) #miejsce na sumę do sprawdzenia
entry1.grid(column=1,row=1,sticky=tk.NS)
btn = tk.Button(content, text="Generuj",command=generuj,bd=10,relief=tk.RIDGE) #dodajemy buton
btn.grid(column=1,row=2,sticky=tk.NW)
lbl_wynik=tk.Label(content, text="Wynik:",bd=5,bg="pink",relief=tk.GROOVE,width=15)
lbl_wynik.grid(column=1,row=5,columnspan=1,rowspan=1,sticky=tk.W)
txt_wynik = scrolledtext.ScrolledText(content,width=13,height=12,bd=3)
txt_wynik.grid(column=1,row=6,rowspan=3,columnspan=1,sticky=tk.W)
btn2 = tk.Button(content, text="Finito",command=on_ok) #przycisk zamykający aplikację
btn2.grid(column=1,row=15,sticky=tk.E)

'''ramka2 = ttk.Frame(win1,borderwidth=5, relief="ridge") #tworzy główną ramkę
ramka2.grid(column=1,row=0,padx=10,sticky=tk.NS) #umieszcza główną ramkę w oknie
lbl3=tk.Label(ramka2, text="Wklej liczbę:",bd=10,bg="light green",relief=tk.RAISED)
lbl3.grid(column=0,row=0,padx=5,pady=5)
lbl4=tk.Label(ramka2, text="Wklej liczbę:",bd=10,bg="light green",relief=tk.RAISED)
lbl4.grid(column=0,row=2,padx=5,pady=5)'''

win1.mainloop()








