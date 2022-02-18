import tkinter as tk #importē GUI tkinter 
from tkcalendar import Calendar #importē kalendāru
from functools import partial #importē funckiju palīgu
import forma #importē moduli forma

window = tk.Tk() #izveido logu
window.title('Salons "Tea time" ') #piešķir logam nosaukumu
window.geometry("400x400") #nodefinē loga lielumu
window.config(bg='#262626') #nomaina fona krāsu

def zina_mirdza(cal,vardi):#funkcija,kas pārbauda Mirdzas noslogojumu
  vardi1=[] #izveido sarakstu,kurā ievietos laiku un datumu
  datue = cal.get_date() #iegūst lietotāja izvēlēto datumu no kalendāra
  date1=str(datue) #nomaina int uz str
  laiks1=str(svar.get())
  vardi1.append(f"{date1} {laiks1}") #pievieno datumu un laiku sarakstam
  if vardi1[0] in vardi: #pārbauda vai nav jau pieraksti uz kādu notiektu laiku
    slikti=tk.Label(window,text="Laiks ir aizņemts",bg="#262626",fg='#FFFFFF',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.8) #paziņojums, ka laiks ir nepieejams
  else:
    labi=tk.Label(window,text="Laiks ir brīvs",bg="#262626",fg='#FFFFFF',font=('Calibri',11),width=30).place(anchor="c",relx=0.5,rely=0.8) #paziņojums, ka laiks ir pieejams
    beigas=tk.Button(window,text="Tālāk >", command=lambda:saraksts(date1,laiks1),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.85,rely=0.9) #poga, kas turpina darbību, izpilda saraksts funkciju

def saraksts(datums1,laiks1):#funkcija, kas ievieto darbinieku noslogojuma sarakstā pierakstus un izsauc formu
    import forma
    specialists="Mirdza" #piešķir mainīgajam speciālista vārdu
    vardi1=f"{datums1} {laiks1}\n" #iedod mainīgajam laika un datuma vērtību
    f=open("mirdza.txt","a") #atver failu
    f.write(vardi1) #ieraksta failā mainīgo vardi1
    f.close() #aizver failu
    a=forma.forma(window,datums1,laiks1,specialists,tips2) #izsauc funkciju forma un padod tai argumentus


def mirdza():#funkcija, kas parāda kalendāru, laiku sarakstu
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
    widgets.destroy()
  global vardi #pasludina vardi par globālo mainīgo
  f = open("mirdza.txt","r") #atver failu ar read metodi
  vardi=[] 
  for x in open ('mirdza.txt','r').readlines(): #nolasa rindiņas jau reģistrēto laiku sarakstā
    vardi.append(x.strip()) #pievieno tos sarakstam, ar kura palīdzību pēc tam salīdzina brīvos laikus
  f.close() #aizver failu
  dat=tk.Label(window,text="Izvēlieties datumu un laiku",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  cal=Calendar(window,selectmode="day",year=2022,month=2,day=3,date_pattern='dd.mm.yy')
  cal.place(anchor="c",relx=0.5,rely=0.4) #ievieto kalendāru
  cal.configure(background='#000000',foreground='#FFFFFF',selectbackground='#ccffa6', selectforeground='#000000',font=('Calibri',10)) #nomaina kalendāra krāsas

  laiki = ['8:00', '10:00', '12:00', '14:00', '16:00'] #izvēlnes saraksta locekļi
  global svar #pasludina svar par globālo mainīgo
  svar = tk.StringVar()
  svar.set(laiki[0]) #sākotnējā vērtība, kas rādās parādoties izvēnei
  def _get(cur): #funkcija, kas iegūst lietotāja izvēlēto laiku
    global svar  
    svar.set(f'{svar.get()}') #iegūst laiku, kuru izvēlējās lietotājs
  drop = tk.OptionMenu(window, svar, command = _get, *laiki)
  drop.place(anchor="c",relx=0.5,rely=0.7)#ievieto laiku izvēlni
  drop.configure(bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11))
  parbaude =tk.Button(window,text="Pārbaudīt",command=lambda:zina_mirdza(cal,vardi),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.9) #poga, kas pārbauda vai laiks ir brīvs, izsauc funkciju zina_mirdza

def zina_talis(cal,vardi):#funkcija,kas pārbauda Tāļa noslogojumu
  vardi1=[] #izveido sarakstu,kurā ievietos laiku un datumu
  datue = cal.get_date() #iegūst lietotāja izvēlēto datumu no kalendāra
  date1=str(datue) #nomaina int uz str
  laiks1=str(svar.get()) #iegūst lietotāja izvēlēto izvēlnes vērtību un pārveido to par str
  vardi1.append(f"{date1} {laiks1}") #pievieno datumu un laiku sarakstam
  if vardi1[0] in vardi: #pārbauda vai nav jau pieraksti uz kādu notiektu laiku
    slikti=tk.Label(window,text="Laiks ir aizņemts",bg="#262626",fg='#FFFFFF',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.8) #paziņojums, ka laiks ir nepieejams
  else:
    labi=tk.Label(window,text="Laiks ir brīvs",bg="#262626",fg='#FFFFFF',font=('Calibri',11),width=30).place(anchor="c",relx=0.5,rely=0.8) #paziņojums, ka laiks ir pieejams
    beigas=tk.Button(window,text="Tālāk >", command=lambda:sarakstst(date1,laiks1),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.85,rely=0.9) #poga, kas turpina darbību, izpilda sarakstst funkciju

def sarakstst(datums1,laiks1): #funkcija, kas ievieto darbinieku noslogojuma sarakstā pierakstus un izsauc formu
    import forma
    specialists="Tālis" #piešķir mainīgajam speciālista vārdu
    vardi1=f"{datums1} {laiks1}\n" #iedod mainīgajam laika un datuma vērtību
    f=open("talis.txt","a") #atver failu
    f.write(vardi1) #ieraksta failā mainīgo vardi1
    f.close() #aizver failu
    a=forma.forma(window,datums1,laiks1,specialists,tips2) #izsauc funkciju forma un padod tai argumentus


def talis(): #funkcija, kas parāda kalendāru, laiku sarakstu
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
    widgets.destroy()
  global vardi #pasludina vardi par globālo mainīgo
  f = open("talis.txt","r")#atver failu ar read metodi
  vardi=[]
  for x in open ('talis.txt','r').readlines(): #nolasa rindiņas jau reģistrēto laiku sarakstā
    vardi.append(x.strip())#pievieno tos sarakstam, ar kura palīdzību pēc tam salīdzina brīvos laikus
  f.close() #aizver failu
  dat=tk.Label(window,text="Izvēlieties datumu un laiku",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  cal=Calendar(window,selectmode="day",year=2022,month=2,day=3,date_pattern='dd.mm.yy')
  cal.place(anchor="c",relx=0.5,rely=0.4) #ievieto kalendāru
  cal.configure(background='#000000',foreground='#FFFFFF',selectbackground='#ccffa6', selectforeground='#000000',font=('Calibri',10))
  #nomaina kalendāra krāsas
  
  laiki = ['8:00', '10:00', '12:00', '14:00', '16:00'] #izvēlnes saraksta locekļi
  global svar #pasludina svar par globālo mainīgo
  svar = tk.StringVar() #sākotnējā vērtība, kas rādās parādoties izvēlnei
  svar.set(laiki[0])
  
  def _get(cur): #funkcija, kas iegūst lietotāja izvēlēto laiku 
    global svar  
    svar.set(f'{svar.get()}')#iegūst laiku, kuru izvēlējās lietotājs
  
  drop = tk.OptionMenu(window, svar, command = _get, *laiki)
  drop.place(anchor="c",relx=0.5,rely=0.7)
  drop.configure(bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)) #ievieto laiku izvēlni
  parbaude =tk.Button(window,text="Pārbaudīt",command=lambda:zina_talis(cal,vardi),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.9) #poga, kas pārbauda vai laiks ir brīvs, izsauc funkciju zina_talis

def zina_juris(cal,vardi):#funkcija,kas pārbauda Jura noslogojumu
  vardi1=[] #izveido sarakstu,kurā ievietos laiku un datumu
  datue = cal.get_date() #iegūst lietotāja izvēlēto datumu no kalendāra
  date1=str(datue) #nomaina int uz str
  laiks1=str(svar.get()) #iegūst lietotāja izvēlēto izvēlnes vērtību un pārveido to par str
  vardi1.append(f"{date1} {laiks1}") #pievieno datumu un laiku sarakstam
  if vardi1[0] in vardi:  #pārbauda vai nav jau pieraksti uz kādu notiektu laiku
    slikti=tk.Label(window,text="Laiks ir aizņemts",bg="#262626",fg='#FFFFFF',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.8) #paziņojums, ka laiks ir nepieejams
  else:
    labi=tk.Label(window,text="Laiks ir brīvs",bg="#262626",fg='#FFFFFF',font=('Calibri',11),width=30).place(anchor="c",relx=0.5,rely=0.8) #paziņojums, ka laiks ir pieejams
    beigas=tk.Button(window,text="Tālāk >", command=lambda:saraksts_juris(date1,laiks1),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.85,rely=0.9)#poga, kas turpina darbību, izpilda saraksts_juris funkciju
    
def saraksts_juris(datums1,laiks1): #funkcija, kas ievieto darbinieku noslogojuma sarakstā pierakstus un izsauc formu
    import forma
    specialists="Juris" #piešķir mainīgajam speciālista vārdu
    vardi1=f"{datums1} {laiks1}\n" #iedod mainīgajam laika un datuma vērtību
    f=open("juris.txt","a") #atver failu
    f.write(vardi1) #ieraksta failā mainīgo vardi1
    f.close() #aizver failu
    a=forma.forma(window,datums1,laiks1,specialists,tips2)  #izsauc funkciju forma un padod tai argumentus


def juris(): #funkcija, kas parāda kalendāru, laiku sarakstu
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
    widgets.destroy()
  global vardi #pasludina vardi par globālo mainīgo
  f = open("juris.txt","r") #atver failu ar read metodi
  vardi=[]
  for x in open ('juris.txt','r').readlines(): #nolasa rindiņas jau reģistrēto laiku sarakstā
    vardi.append(x.strip()) #pievieno tos sarakstam, ar kura palīdzību pēc tam salīdzina brīvos laikus
  f.close() #aizver failu
  dat=tk.Label(window,text="Izvēlieties datumu un laiku",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  cal=Calendar(window,selectmode="day",year=2022,month=2,day=3,date_pattern='dd.mm.yy')
  cal.place(anchor="c",relx=0.5,rely=0.4) #ievieto kalendāru
  cal.configure(background='#000000',foreground='#FFFFFF',selectbackground='#ccffa6', selectforeground='#000000',font=('Calibri',10))
  #nomaina kalendāra krāsas

  laiki = ['8:00', '10:00', '12:00', '14:00', '16:00'] #izvēlnes saraksta locekļi
  global svar #pasludina svar par globālo mainīgo
  svar = tk.StringVar()
  svar.set(laiki[0]) #sākotnējā vērtība, kas rādās parādoties izvēlnei
  def _get(cur): #funkcija, kas iegūst lietotāja izvēlēto laiku 
    global svar  
    svar.set(f'{svar.get()}')#iegūst laiku, kuru izvēlējās lietotājs 
  drop = tk.OptionMenu(window, svar, command = _get, *laiki)
  drop.place(anchor="c",relx=0.5,rely=0.7) #ievieto laiku izvēlni
  drop.configure(bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11))
  parbaude =tk.Button(window,text="Pārbaudīt",command=lambda:zina_juris(cal,vardi),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.9) #poga, kas pārbauda vai laiks ir brīvs, izsauc funkciju zina_talis

def zina_maija(cal,vardi):#funkcija,kas pārbauda Maijas noslogojumu
  vardi1=[] #izveido sarakstu,kurā ievietos laiku un datumu
  datue = cal.get_date() #iegūst lietotāja izvēlēto datumu no kalendāra
  date1=str(datue) #nomaina int uz str
  laiks1=str(svar.get())  #iegūst lietotāja izvēlēto izvēlnes vērtību un pārveido to par str
  vardi1.append(f"{date1} {laiks1}") #pievieno datumu un laiku sarakstam
  if vardi1[0] in vardi:  #pārbauda vai nav jau pieraksti uz kādu notiektu laiku
    slikti=tk.Label(window,text="Laiks ir aizņemts",bg="#262626",fg='#FFFFFF',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.8) #paziņojums, ka laiks ir nepieejams
  else:
    labi=tk.Label(window,text="Laiks ir brīvs",bg="#262626",fg='#FFFFFF',font=('Calibri',11),width=30).place(anchor="c",relx=0.5,rely=0.8)#paziņojums, ka laiks ir pieejams
    beigas=tk.Button(window,text="Tālāk >", command=lambda:saraksts_maija(date1,laiks1),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.85,rely=0.9) #poga, kas turpina darbību, izpilda saraksts_maija funkciju

def saraksts_maija(datums1,laiks1): #funkcija, kas ievieto darbinieku noslogojuma sarakstā pierakstus un izsauc formu
    import forma
    specialists="Maija" #piešķir mainīgajam speciālista vārdu
    vardi1=f"{datums1} {laiks1}\n" #iedod mainīgajam laika un datuma vērtību
    f=open("maija.txt","a") #atver failu
    f.write(vardi1) #ieraksta failā mainīgo vardi1
    f.close()  #aizver failu
    a=forma.forma(window,datums1,laiks1,specialists,tips2)  #izsauc funkciju forma un padod tai argumentus


def maija(): #funkcija, kas parāda kalendāru, laiku sarakstu
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
    widgets.destroy()
  global vardi #pasludina vardi par globālo mainīgo
  f = open("maija.txt","r") #atver failu ar read metodi
  vardi=[]
  for x in open ('maija.txt','r').readlines(): #nolasa rindiņas jau reģistrēto laiku sarakstā
    vardi.append(x.strip()) #pievieno tos sarakstam, ar kura palīdzību pēc tam salīdzina brīvos laikus
  f.close() #aizver failu
  dat=tk.Label(window,text="Izvēlieties datumu un laiku",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  cal=Calendar(window,selectmode="day",year=2022,month=2,day=3,date_pattern='dd.mm.yy')
  cal.place(anchor="c",relx=0.5,rely=0.4)
  #ievieto kalendāru
  cal.configure(background='#000000',foreground='#FFFFFF',selectbackground='#ccffa6', selectforeground='#000000',font=('Calibri',10))
  #nomaina kalendāra krāsas

  laiki = ['8:00', '10:00', '12:00', '14:00', '16:00']  #izvēlnes saraksta locekļi
  global svar #pasludina svar par globālo mainīgo
  svar = tk.StringVar()
  svar.set(laiki[0]) #sākotnējā vērtība, kas rādās parādoties izvēlnei
  def _get(cur):   #funkcija, kas iegūst lietotāja izvēlēto laiku 
    global svar  
    svar.set(f'{svar.get()}') #iegūst laiku, kuru izvēlējās lietotājs 
  drop = tk.OptionMenu(window, svar, command = _get, *laiki)
  drop.place(anchor="c",relx=0.5,rely=0.7)
  drop.configure(bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11))
  #ievieto laiku izvēlni
  parbaude =tk.Button(window,text="Pārbaudīt",command=lambda:zina_maija(cal,vardi),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.9)  #poga, kas pārbauda vai laiks ir brīvs, izsauc funkciju zina_maija

  
def frizieri_spec(tips):#funkcija,kas parāda frizierus
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
    widgets.destroy()
  global tips2 #pasludina tips2 par globālo mainīgo
  tips1=tk.StringVar()
  tips1.set(tips) #nomaina tips1 uz iepriekšējās 'lapas' izdarīto izvēli
  tips2=tips1.get() #iegust tips1 vērtību
  tips=tk.Label(window, text="Izvēlieties speciālistu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  izv1 = tk.Button(window, text="Maija",command=maija,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.2) #poga,kas norāda uz spec. Maiju, izsauc funkciju Maija
  izv1 = tk.Button(window, text="Juris",command=juris,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.3) #poga,kas norāda uz spec. Juris, izsauc funkciju Juris
  
def masieri_spec(tips):#funkcija,kas parāda masierus
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
    widgets.destroy()
  global tips2
  tips1=tk.StringVar()
  tips1.set(tips) #nomaina tips1 uz iepriekšējās 'lapas' izdarīto izvēli
  tips2=tips1.get() #iegust tips1 vērtību
  tips=tk.Label(window, text="Izvēlieties speciālistu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  izv1 = tk.Button(window, text="Tālis",command=talis,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.2) #poga,kas norāda uz spec. Tāli, izsauc funkciju Talis
  izv1 = tk.Button(window, text="Mirdza",command=mirdza,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.3) #poga,kas norāda uz spec. Mirdzu, izsauc funkciju Mirdza
  atpakal=tk.Button(window, text="< Atpakaļ",command=masaza,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) #poga, kas atļauj veikt atpakaļ darbību, atgriežas iepriekšējā lapā

def v_pakal(): #funkcija, kas norāda visus vīriešu frizieru pakalpojumus
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
        widgets.destroy()
  vkontura="Vīriešu matu kontūras veidošana"
  vnoskusana="Vīriešu matu noskūšana"
  vkrasosana="Vīriešu matu krāsošana"
  #piešķir mainīgajiem pakalpojuma tipus, lai varētu tos iedod, kā argumetus izsaucot funkciju frizieri_spec
  tips=tk.Label(window, text="Izvēlieties pakalpojuma tipu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  kontrura=tk.Label(window, text="Matu kontūras veidošana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.2) #pakalpojuma nosaukums
  noskusana=tk.Label(window, text="Matu noskūšana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.3) #pakalpojuma nosaukums
  krasosana=tk.Label(window, text="Matu krāsošana- no 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.4) #pakalpojuma nosaukums
  izv1 = tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,vkontura),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.2) #poga, kas izsauc funkciju frizieri_spec un iedod tai argumentu-vkontura
  izv2= tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,vnoskusana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.3) #poga, kas izsauc funkciju frizieri_spec un iedod tai argumentu-vnoskusana
  izv3= tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,vkrasosana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.4) #poga, kas izsauc funkciju frizieri_spec un iedod tai argumentu-vkrasosana
  atpakal=tk.Button(window, text="< Atpakaļ",command=frizieri,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) 
  #poga, kas atļauj veikt atpakaļ darbību, atgriežas iepriekšējā lapā


def s_pakal(): #funkcija, kas norāda visus sieviešu frizieru pakalpojumus
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
        widgets.destroy()
  sgriesana="Sieviešu matu griešana"
  sgr_kr="Sieviešu matu griešana, krāsošana"
  spieaudz="Sieviešu matu pieaudzēšana"
  #piešķir mainīgajiem pakalpojuma tipus, lai varētu tos iedod, kā argumetus izsaucot funkciju frizieri_spec
  tips=tk.Label(window, text="Izvēlieties pakalpojuma tipu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  griez=tk.Label(window, text="Matu griešana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.2) #pakalpojuma nosaukums
  kr_griez=tk.Label(window, text="Matu griešana un krāsošana-\n no 20€",bg='#262626',fg='#FFFFFF',font=('Calibri',11))  .place(anchor="w",relx=0.02,rely=0.3) #pakalpojuma nosaukums
  pieaud=tk.Label(window, text="Matu pieaudzēšana- no 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.4) #pakalpojuma nosaukums
  izv1 = tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,sgriesana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.2) #poga, kas izsauc funkciju frizieri_spec un iedod tai argumentu-sgriesana
  izv2= tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,sgr_kr),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.3) #poga, kas izsauc funkciju frizieri_spec un iedod tai argumentu-sgr_kr
  izv3= tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,spieaudz),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.4) #poga, kas izsauc funkciju frizieri_spec un iedod tai argumentu-spieaudz
  atpakal=tk.Button(window, text="< Atpakaļ",command=frizieri,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) #poga, kas atļauj veikt atpakaļ darbību, atgriežas iepriekšējā lapā
 

def b_pakal(): #funkcija, kas norāda visus bērnu frizieru pakalpojumus
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
        widgets.destroy()
  bnoskusana="Bērnu matu noskusana"
  bapgriesana="Bērnu matu apgriešana"
  bkrasošana="Matu šķipsnu krāsošana"
  #piešķir mainīgajiem pakalpojuma tipus, lai varētu tos iedod, kā argumetus izsaucot funkciju frizieri_spec
  tips=tk.Label(window, text="Izvēlieties pakalpojuma tipu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  nosk=tk.Label(window, text="Matu noskūšana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.2) #pakalpojuma nosaukums
  apgrie=tk.Label(window, text="Matu apgriešana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.3) #pakalpojuma nosaukums
  skipsna=tk.Label(window, text="Matu šķipsnu krāsošana- 5€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.4) #pakalpojuma nosaukums
  izv1= tk.Button(window, text="Izvēlēties",command=partial(frizieri_spec,bnoskusana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.2) #poga, kas izsauc funkciju frizieri_spec un iedod tai argumentu-bnoskusana
  izv2= tk.Button(window, text="Izvēlēties",command=partial(frizieri_spec,bapgriesana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.3) #poga, kas izsauc funkciju frizieri_spec un iedod tai argumentu-bapgriesana
  izv3= tk.Button(window, text="Izvēlēties",command=partial(frizieri_spec,bkrasošana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.4)#poga, kas izsauc funkciju frizieri_spec un iedod tai argumentu-bkrasosana
  atpakal=tk.Button(window, text="< Atpakaļ",command=frizieri,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) #poga, kas atļauj veikt atpakaļ darbību, atgriežas iepriekšējā lapā


def frizieri(): #funkcija,kas parāda frizieru pakalpojumu veidus
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
        widgets.destroy()
  tips=tk.Label(window, text="Izvēlieties pakalpojuma veidu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  sieviesu = tk.Button(window, text="Sieviešu",command=s_pakal,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.2) #poga, kas izsauc funkciju s_pakal- pakalpojumi sievietēm
  viriesu= tk.Button(window, text="Vīriešu",command=v_pakal,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.3) #poga, kas izsauc funkciju v_pakal- pakalpojumi vīriešiem
  bernu= tk.Button(window, text="Bērnu",command=b_pakal,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.4) #poga, kas izsauc funkciju b_pakal- pakalpojumi bērniem
  atpakal=tk.Button(window, text="< Atpakaļ",command=sakums,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) #poga, kas atļauj veikt atpakaļ darbību, atgriežas iepriekšējā lapā


def masaza(): #funkcija, kas norāda visus masieru pakalpojumus
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
        widgets.destroy()
  mmedus="Medus masāža"
  mspeka="Spēka masāža"
  msokolades="Šokolādes masāža"
    #piešķir mainīgajiem pakalpojuma tipus, lai varētu tos iedod, kā argumetus izsaucot funkciju masieri_spec
  tips=tk.Label(window, text="Izvēlieties pakalpojuma tipu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  medus=tk.Label(window, text="Medus masāža- 20€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.05,rely=0.2) #pakalpojuma nosaukums
  speka=tk.Label(window, text="Spēka masāža- 25€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.05,rely=0.3) #pakalpojuma nosaukums
  sokolades=tk.Label(window, text="Šokolādes masāža- 35€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.05,rely=0.4) #pakalpojuma nosaukums
  izv1 = tk.Button(window, text="Izvēlēties",command=partial (masieri_spec,mmedus),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.2) #poga, kas izsauc funkciju masieri_spec un iedod tai argumentu-mmedus/Medus masāža
  izv2= tk.Button(window, text="Izvēlēties",command=partial (masieri_spec,mspeka),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.3) #poga, kas izsauc funkciju masieri_spec un iedod tai argumentu-mspeka/Spēka masāža
  izv3= tk.Button(window, text="Izvēlēties",command=partial (masieri_spec,msokolades),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.4) #poga, kas izsauc funkciju masieri_spec un iedod tai argumentu-msokolades/Šokolādes masāža
  text=tk.Button(window,text="< Atpakaļ",command=sakums,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) #poga, kas atļauj veikt atpakaļ darbību, atgriežas iepriekšējā lapā


def sakums(): #funkcija, kas parāda pieejamos pakalpojuma veidus salonā
  for widgets in window.winfo_children(): #nodzēš visu nost no loga
        widgets.destroy()
  pakalpojumi = tk.Label(text="Izvēlieties pakalpojumu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1) #sadaļas nosaukums
  frizieris = tk.Button(window, text="Frizieris",command=frizieri,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.2) #poga,kas norāda uz Friziera pakalpojumiem, izsauc funkciju frizieri
  masieris= tk.Button(window, text="Masieris",command=masaza,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.3) #poga,kas norāda uz Masiera pakalpojumiem, izsauc funkciju masaza
  

hello = tk.Label(text="Sveicināti!",bg='#262626',fg='#ccffa6',font=('Calibri',14)).place(anchor="c",relx=0.5,rely=0.1) #sasveicināšanas 
hello1 = tk.Label(text="Mūsu salona darba laiks ir Pr.- Sv. 8:00-18:00",bg='#262626',fg='#ccffa6',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.16) #paziņojums
button = tk.Button(window, text="Veikt pierakstu",command=sakums,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.25) #poga,kas ļauj sāk pieraksta veikšanas procesu, izsauc funkciju sakums 
tk.mainloop()