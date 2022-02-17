import tkinter as tk
import csv
from tkinter import *

def forma(window,datums1,laiks1,specialists,pakalpojums):
  for widgets in window.winfo_children():
    widgets.destroy()
    
  def cipari(input):
    return all(char.isdigit() or char.isspace() for char in input)

  def burti(input):
    return all(char.isalpha() or char.isspace() for char in input)
    
  def epasts(input):
    return all(char.isalpha() or char.isdigit() for char in input) or input=="." or input=="@"
 


  def registracija():
      pieraksts=f'{laiks.get()}'
      sniedzejs=f'{meistars.get()}'
      pakalp=f'{pakalpojums1.get()}'
      vards=f'{vards1.get()}'
      uzvards=f'{uzvards1.get()}'
      telefons=f'{telefons1.get()}'
      epasts=f'{epasts1.get()}'
      if len(vards)==0:
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.3)
      elif len(uzvards)==0:
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.4)
      elif len(telefons)==0 :
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.5)
      elif len(epasts)==0:
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.6)
      else:
        dati=[pieraksts,sniedzejs,pakalp,vards,uzvards,telefons,epasts]
        with open('registracija.csv','a',encoding='UTF8') as f:
          writer=csv.writer(f)
          writer.writerow(dati)
        for widgets in window.winfo_children():
          widgets.destroy()
        paldies=tk.Label(window,text="Pieraksts veiksmīgi reģistrēts!\n Uz drīzu tikšanos!",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.5)
  global meistars
  global laiks
  pakalpojums1=tk.StringVar()
  pakalpojums1.set(f"{pakalpojums}")
  meistars = tk.StringVar()
  meistars.set(specialists)
  laiks = tk.StringVar()
  laiks.set(f"{datums1}-{laiks1}")
  vards1=tk.StringVar() 
  uzvards1=tk.StringVar() 
  telefons1=tk.StringVar() 
  epasts1=tk.StringVar()
  Beigas = tk.Label(window ,text = "Pabeidziet pierakstu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.05)
  dat = tk.Label(window ,text = "Datums, Laiks:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.15)
  dat1 = tk.Label(window,textvariable=laiks,bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.15)
  a = tk.Label(window ,text = "Vārds:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.25)
  b = tk.Label(window ,text = "Uzvārds:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.35)
  c = tk.Label(window ,text = "Telefona numurs:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.45)
  d = tk.Label(window ,text = "E-Pasts:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.55)
  pakalpojumse=tk.Label(window ,text = "Pakalpojums:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.65)
  pakal= tk.Label(window,textvariable=pakalpojums1,wraplength=170,bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.65,width=200)
  specialists=tk.Label(window ,text = "Meistars:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.75)
  spec= tk.Label(window,textvariable=meistars,bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.75,width=150)
  b_parbaude=window.register(burti)
  vardsievade = tk.Entry(window,textvariable=vards1,validatecommand=(b_parbaude,'%S'),font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.25,width=150)
  uzvardsievade = tk.Entry(window,textvariable=uzvards1,validatecommand=(b_parbaude,'%S'),font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.35,width=150)

  c_parbaude=window.register(cipari)
  telefonsievade = tk.Entry(window,textvariable=telefons1,validate="key",validatecommand=(c_parbaude,'%S'),font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.45,width=150)
  e_parbaude=window.register(epasts)
  epastsievade = tk.Entry(window,textvariable=epasts1,validate='key',validatecommand=(e_parbaude,'%S'),font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.55,width=150)
  talak=tk.Button(window, text="Reģistrēt pierakstu",command=registracija,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',10)).place(anchor="c",relx=0.5,rely=0.9)
  reg=window.register(cipari)
    
