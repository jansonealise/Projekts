import tkinter as tk #importē GUI tkinter
import csv #importē csv
from tkinter import *

def forma(window,datums1,laiks1,specialists,pakalpojums):
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
    widgets.destroy()
    
  def cipari(input): #pārbauda, vai ievadīti tiek tikai cipari
    return all(char.isdigit() or char.isspace() for char in input)

  def burti(input): #pārbauda, vai tiek ievadīti burti
    return all(char.isalpha() or char.isspace() for char in input)
    
  def epasts(input): #parbauda, vai tiek izmantotas atļautās rakstzīmes e-pastam
    return all(char.isalpha() or char.isdigit() for char in input) or input=="." or input=="@"
 


  def registracija(): #funkcija, kas pārbauda vai ievades lauki ir aizpildīti un informācijas datu ievade failā
      pieraksts=f'{laiks.get()}' #pieraksts iegūst laiks vērtību
      sniedzejs=f'{meistars.get()}' #sniedzejs iegūst meistars vērtību
      pakalp=f'{pakalpojums1.get()}' #pakal iegūst pakalpojums1 vērtību
      vards=f'{vards1.get()}' #vards iegūst vards1 vērtību
      uzvards=f'{uzvards1.get()}' #uzvards iegūst uzvards1 vērtību
      telefons=f'{telefons1.get()}'#telefons iegūst telefons1 vērtību
      epasts=f'{epasts1.get()}' #epasts iegūst epasts1 vērtību
      if len(vards)==0: #parbauda, vai lietotājs nav atstājis tukšumu
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.3)
      elif len(vards)<3: #parbauda, vai lietotājs nav ierakstījis par maz rakstzīmes(mazākais burtu skaits latv.val. cilvēka vārdā ir 3)
        a = tk.Label(window ,text = "Par maz rakstzīmju",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.3)
      elif len(uzvards)==0: #parbauda, vai lietotājs nav atstājis tukšumu
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.4)
      elif len(uzvards)<3: #parbauda, vai lietotājs nav ierakstījis par maz rakstzīmes
        a = tk.Label(window ,text = "Par maz rakstzīmju",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.4)
      elif len(telefons)==0 :#parbauda, vai lietotājs nav atstājis tukšumu
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.5)
      elif len(telefons)<8:
         #parbauda, vai lietotājs nav ierakstījis par maz rakstzīmes
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.6,rely=0.5)
      elif len(telefons)>8:
         #parbauda, vai lietotājs nav ierakstījis par maz rakstzīmes
        a = tk.Label(window ,text = "Par daudz rakstzīmju",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.6,rely=0.5)
      elif len(epasts)==0: #parbauda, vai lietotājs nav atstājis tukšumu
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.6)
      elif "@" not in epasts: #parbauda, vai lietotājs ir ievadījis e-pastu
        a = tk.Label(window ,text = "Obligāts lauks",bg='#262626',fg='#FFFFFF',font=('Calibri',7)).place(anchor="w",relx=0.65,rely=0.6)
      else:
        dati=[pieraksts,sniedzejs,pakalp,vards,uzvards,telefons,epasts] #csv failā ievadītie dati
        with open('registracija.csv','a',encoding='UTF8') as f: #atver csv, lai taja ierakstītu informāciju
          writer=csv.writer(f) 
          writer.writerow(dati) #ieraksta csv failā informāciju
        for widgets in window.winfo_children(): #nodzēš visu no loga
          widgets.destroy()
        paldies=tk.Label(window,text='Pieraksts veiksmīgi reģistrēts!\n Uz drīzu tikšanos,\n salonā "Tea time"! ',bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.5) #apstiprinājuma paziņojums
  global meistars
  global laiks
  pakalpojums1=tk.StringVar()
  pakalpojums1.set(f"{pakalpojums}") #iedod pakalpojums1 vērtību pakalpojums
  meistars = tk.StringVar()
  meistars.set(specialists)#iedod meistars vērtību specialists
  laiks = tk.StringVar()
  laiks.set(f"{datums1}-{laiks1}") #iedod laiks vērtību datums1-laiks1
  vards1=tk.StringVar() 
  uzvards1=tk.StringVar() 
  telefons1=tk.StringVar() 
  epasts1=tk.StringVar()
  Beigas = tk.Label(window ,text = "Pabeidziet pierakstu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.05) #sadaļas nosaukums
  dat = tk.Label(window ,text = "Datums, Laiks:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.15) #etiķete-datums un laiks
  dat1 = tk.Label(window,textvariable=laiks,bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.15) #parāda pieraksta datumu un laiku 
  a = tk.Label(window ,text = "Vārds:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.25) #etiķete-vārds
  b = tk.Label(window ,text = "Uzvārds:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.35) #etiķete-uzvārds
  c = tk.Label(window ,text = "Telefona numurs:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.45) #etiķete-telefona numurs
  d = tk.Label(window ,text = "E-Pasts:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.55) #etiķete-e-pasts
  pakalpojumse=tk.Label(window ,text = "Pakalpojums:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.65) #etiķete-pakalpojums
  pakal= tk.Label(window,textvariable=pakalpojums1,wraplength=170,bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.65,width=200) #parāda lietotāja izvēlēto pakalpojumu
  specialists=tk.Label(window ,text = "Meistars:",bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="w",relx=0.05,rely=0.75) #etiķete-meistars
  spec= tk.Label(window,textvariable=meistars,bg='#262626',fg='#FFFFFF',font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.75,width=150) #parāda lietotāja izvēlēto meistaru
  b_parbaude=window.register(burti) #reģistrē funkciju kā veidu kā pārbaudīt ievadīto informāciju
  vardsievade = tk.Entry(window,textvariable=vards1,validatecommand=(b_parbaude,'%S'),font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.25,width=150) #ievades lauks vārdam
  uzvardsievade = tk.Entry(window,textvariable=uzvards1,validatecommand=(b_parbaude,'%S'),font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.35,width=150) #ievades lauks uzvārdam

  c_parbaude=window.register(cipari)#reģistrē funkciju kā veidu kā pārbaudīt ievadīto informāciju
  telefonsievade = tk.Entry(window,textvariable=telefons1,validate="key",validatecommand=(c_parbaude,'%S'),font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.45,width=150) #ievades lauks telefona numuram

  e_parbaude=window.register(epasts) #reģistrē funkciju kā veidu kā pārbaudīt ievadīto informāciju
  epastsievade = tk.Entry(window,textvariable=epasts1,validate='key',validatecommand=(e_parbaude,'%S'),font=('Calibri',10)).place(anchor="c",relx=0.65,rely=0.55,width=150)#ievades lauks e-pastam

  registret=tk.Button(window, text="Reģistrēt pierakstu",command=registracija,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',10)).place(anchor="c",relx=0.5,rely=0.9)#poga, kas izsauc funkciju registracija,kas pārbauda vai lietotājs visu ir ievadījis pareizi un ievada datus csv failā