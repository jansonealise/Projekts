import tkinter as tk
from tkcalendar import Calendar
from functools import partial
import forma

window = tk.Tk()
window.title('Salons "Tea time" ')
window.geometry("400x400")
window.config(bg='#262626')

def zina_mirdza(cal,vardi):
  vardi1=[]
  datue = cal.get_date()
  date1=str(datue)
  laiks1=str(svar.get())
  vardi1.append(f"{date1} {laiks1}")
  if vardi1[0] in vardi:
    slikti=tk.Label(window,text="Laiks ir aizņemts",bg="#262626",fg='#FFFFFF',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.8)
  else:
    labi=tk.Label(window,text="Laiks ir brīvs",bg="#262626",fg='#FFFFFF',font=('Calibri',11),width=30).place(anchor="c",relx=0.5,rely=0.8)
    beigas=tk.Button(window,text="Tālāk >", command=lambda:saraksts(date1,laiks1),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.85,rely=0.9)

def saraksts(datums1,laiks1):
    import forma
    specialists="Mirdza"
    vardi1=f"{datums1} {laiks1}\n"
    f=open("mirdza.txt","a")
    f.write(vardi1)
    f.close()
    a=forma.forma(window,datums1,laiks1,specialists,tips2)


def mirdza():
  for widgets in window.winfo_children():
    widgets.destroy()
  global vardi
  f = open("mirdza.txt","r")
  vardi=[]
  for x in open ('mirdza.txt','r').readlines():
    vardi.append(x.strip())
  f.close()
  dat=tk.Label(window,text="Izvēlieties datumu un laiku",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  cal=Calendar(window,selectmode="day",year=2022,month=2,day=3,date_pattern='dd.mm.yy')
  cal.place(anchor="c",relx=0.5,rely=0.4)
  cal.configure(background='#000000',foreground='#FFFFFF',selectbackground='#ccffa6', selectforeground='#000000',font=('Calibri',10))

  laiki = ['8:00', '10:00', '12:00', '14:00', '16:00']
  global svar
  svar = tk.StringVar()
  svar.set(laiki[0])
  def _get(cur):  
    global svar  
    svar.set(f'{svar.get()}')  
  drop = tk.OptionMenu(window, svar, command = _get, *laiki)
  drop.place(anchor="c",relx=0.5,rely=0.7)
  drop.configure(bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11))
  parbaude =tk.Button(window,text="Pārbaudīt",command=lambda:zina_mirdza(cal,vardi),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.9)
  atpakal=tk.Button(window, text="< Atpakaļ",command=masieri_spec,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9)

def zina_talis(cal,vardi):
  vardi1=[]
  datue = cal.get_date()
  date1=str(datue)
  laiks1=str(svar.get())
  vardi1.append(f"{date1} {laiks1}")
  if vardi1[0] in vardi:
    slikti=tk.Label(window,text="Laiks ir aizņemts",bg="#262626",fg='#FFFFFF',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.8)
  else:
    labi=tk.Label(window,text="Laiks ir brīvs",bg="#262626",fg='#FFFFFF',font=('Calibri',11),width=30).place(anchor="c",relx=0.5,rely=0.8)
    beigas=tk.Button(window,text="Tālāk >", command=lambda:sarakstst(date1,laiks1),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.85,rely=0.9)

def sarakstst(datums1,laiks1):
    import forma
    specialists="Tālis"
    vardi1=f"{datums1} {laiks1}\n"
    f=open("talis.txt","a")
    f.write(vardi1)
    f.close()
    a=forma.forma(window,datums1,laiks1,specialists,tips2)


def talis():
  for widgets in window.winfo_children():
    widgets.destroy()
  global vardi
  f = open("talis.txt","r")
  vardi=[]
  for x in open ('talis.txt','r').readlines():
    vardi.append(x.strip())
  f.close()
  dat=tk.Label(window,text="Izvēlieties datumu un laiku",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  cal=Calendar(window,selectmode="day",year=2022,month=2,day=3,date_pattern='dd.mm.yy')
  cal.place(anchor="c",relx=0.5,rely=0.4)
  cal.configure(background='#000000',foreground='#FFFFFF',selectbackground='#ccffa6', selectforeground='#000000',font=('Calibri',10))

  
  laiki = ['8:00', '10:00', '12:00', '14:00', '16:00']
  global svar
  svar = tk.StringVar()
  svar.set(laiki[0])
  
  def _get(cur):  
    global svar  
    svar.set(f'{svar.get()}')
  
  drop = tk.OptionMenu(window, svar, command = _get, *laiki)
  drop.place(anchor="c",relx=0.5,rely=0.7)
  drop.configure(bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11))
  parbaude =tk.Button(window,text="Pārbaudīt",command=lambda:zina_talis(cal,vardi),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.9)
  atpakal=tk.Button(window, text="< Atpakaļ",command=masieri_spec,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) 

def zina_juris(cal,vardi):
  vardi1=[]
  datue = cal.get_date()
  date1=str(datue)
  laiks1=str(svar.get())
  vardi1.append(f"{date1} {laiks1}")
  if vardi1[0] in vardi:
    slikti=tk.Label(window,text="Laiks ir aizņemts",bg="#262626",fg='#FFFFFF',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.8)
  else:
    labi=tk.Label(window,text="Laiks ir brīvs",bg="#262626",fg='#FFFFFF',font=('Calibri',11),width=30).place(anchor="c",relx=0.5,rely=0.8)
    beigas=tk.Button(window,text="Tālāk >", command=lambda:saraksts_juris(date1,laiks1),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.85,rely=0.9)

def saraksts_juris(datums1,laiks1):
    import forma
    specialists="Juris"
    vardi1=f"{datums1} {laiks1}\n"
    f=open("juris.txt","a")
    f.write(vardi1)
    f.close()
    a=forma.forma(window,datums1,laiks1,specialists,tips2)


def juris():
  for widgets in window.winfo_children():
    widgets.destroy()
  global vardi
  f = open("juris.txt","r")
  vardi=[]
  for x in open ('juris.txt','r').readlines():
    vardi.append(x.strip())
  f.close()
  dat=tk.Label(window,text="Izvēlieties datumu un laiku",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  cal=Calendar(window,selectmode="day",year=2022,month=2,day=3,date_pattern='dd.mm.yy')
  cal.place(anchor="c",relx=0.5,rely=0.4)
  cal.configure(background='#000000',foreground='#FFFFFF',selectbackground='#ccffa6', selectforeground='#000000',font=('Calibri',10))

  laiki = ['8:00', '10:00', '12:00', '14:00', '16:00']
  global svar
  svar = tk.StringVar()
  svar.set(laiki[0])
  def _get(cur):  
    global svar  
    svar.set(f'{svar.get()}')   
  drop = tk.OptionMenu(window, svar, command = _get, *laiki)
  drop.place(anchor="c",relx=0.5,rely=0.7)
  drop.configure(bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11))
  parbaude =tk.Button(window,text="Pārbaudīt",command=lambda:zina_juris(cal,vardi),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.9)
  atpakal=tk.Button(window, text="< Atpakaļ",command=frizieri_spec,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) 

def zina_maija(cal,vardi):
  vardi1=[]
  datue = cal.get_date()
  date1=str(datue)
  laiks1=str(svar.get())
  vardi1.append(f"{date1} {laiks1}")
  if vardi1[0] in vardi:
    slikti=tk.Label(window,text="Laiks ir aizņemts",bg="#262626",fg='#FFFFFF',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.8)
  else:
    labi=tk.Label(window,text="Laiks ir brīvs",bg="#262626",fg='#FFFFFF',font=('Calibri',11),width=30).place(anchor="c",relx=0.5,rely=0.8)
    beigas=tk.Button(window,text="Tālāk >", command=lambda:saraksts_maija(date1,laiks1),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.85,rely=0.9)

def saraksts_maija(datums1,laiks1):
    import forma
    specialists="Maija"
    vardi1=f"{datums1} {laiks1}\n"
    f=open("maija.txt","a")
    f.write(vardi1)
    f.close()
    a=forma.forma(window,datums1,laiks1,specialists,tips2)


def maija():
  for widgets in window.winfo_children():
    widgets.destroy()
  global vardi
  f = open("maija.txt","r")
  vardi=[]
  for x in open ('maija.txt','r').readlines():
    vardi.append(x.strip())
  f.close()
  dat=tk.Label(window,text="Izvēlieties datumu un laiku",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  cal=Calendar(window,selectmode="day",year=2022,month=2,day=3,date_pattern='dd.mm.yy')
  cal.place(anchor="c",relx=0.5,rely=0.4)
  cal.configure(background='#000000',foreground='#FFFFFF',selectbackground='#ccffa6', selectforeground='#000000',font=('Calibri',10))

  laiki = ['8:00', '10:00', '12:00', '14:00', '16:00']
  global svar
  svar = tk.StringVar()
  svar.set(laiki[0])
  def _get(cur):  
    global svar  
    svar.set(f'{svar.get()}')   
  drop = tk.OptionMenu(window, svar, command = _get, *laiki)
  drop.place(anchor="c",relx=0.5,rely=0.7)
  drop.configure(bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11))

  parbaude =tk.Button(window,text="Pārbaudīt",command=lambda:zina_maija(cal,vardi),bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.9)
  atpakal=tk.Button(window, text="< Atpakaļ",command=frizieri_spec,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) 

  
def frizieri_spec(tips):
  for widgets in window.winfo_children():
    widgets.destroy()
  global tips2
  tips1=tk.StringVar()
  tips1.set(tips)
  tips2=tips1.get()
  tips=tk.Label(window, text="Izvēlieties speciālistu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  izv1 = tk.Button(window, text="Maija",command=maija,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.2)
  izv1 = tk.Button(window, text="Juris",command=juris,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.3)
  
def masieri_spec(tips):
  for widgets in window.winfo_children():
    widgets.destroy()
  global tips2
  tips1=tk.StringVar()
  tips1.set(tips)
  tips2=tips1.get()
  tips=tk.Label(window, text="Izvēlieties speciālistu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  izv1 = tk.Button(window, text="Tālis",command=talis,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.2)
  izv1 = tk.Button(window, text="Mirdza",command=mirdza,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.3)
  atpakal=tk.Button(window, text="< Atpakaļ",command=masaza,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) 

def v_pakal():
  for widgets in window.winfo_children():
        widgets.destroy()
  vkontura="Vīriešu matu kontūras veidošana"
  vnoskusana="Vīriešu matu noskūšana"
  vkrasosana="Vīriešu matu krāsošana"
  tips=tk.Label(window, text="Izvēlieties pakalpojuma tipu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  kontrura=tk.Label(window, text="Matu kontūras veidošana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.2)
  noskusana=tk.Label(window, text="Matu noskūšana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.3)
  krasosana=tk.Label(window, text="Matu krāsošana- no 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.4)
  izv1 = tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,vkontura),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.2)
  izv2= tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,vnoskusana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.3)
  izv3= tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,vkrasosana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.4)
  atpakal=tk.Button(window, text="< Atpakaļ",command=frizieri,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9) 


def s_pakal():
  for widgets in window.winfo_children():
        widgets.destroy()
  sgriesana="Sieviešu matu griešana"
  sgr_kr="Sieviešu matu griešana, krāsošana"
  spieaudz="Sieviešu matu pieaudzēšana"
  tips=tk.Label(window, text="Izvēlieties pakalpojuma tipu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  griez=tk.Label(window, text="Matu griešana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.2)
  kr_griez=tk.Label(window, text="Matu griešana un krāsošana-\n no 20€",bg='#262626',fg='#FFFFFF',font=('Calibri',11))  .place(anchor="w",relx=0.02,rely=0.3)
  pieaud=tk.Label(window, text="Matu pieaudzēšana- no 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.4)
  izv1 = tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,sgriesana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.2)
  izv2= tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,sgr_kr),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.3)
  izv3= tk.Button(window, text="Izvēlēties",command= partial(frizieri_spec,spieaudz),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.4)
  atpakal=tk.Button(window, text="< Atpakaļ",command=frizieri,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9)  

def b_pakal():
  for widgets in window.winfo_children():
        widgets.destroy()
  bnoskusana="Bērnu matu noskusana"
  bapgriesana="Bērnu matu apgriešana"
  bkrasošana="Matu šķipsnu krāsošana"
  tips=tk.Label(window, text="Izvēlieties pakalpojuma tipu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  nosk=tk.Label(window, text="Matu noskūšana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.2)
  apgrie=tk.Label(window, text="Matu apgriešana- 10€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.3)
  skipsna=tk.Label(window, text="Matu šķipsnu krāsošana- 5€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.02,rely=0.4)
  izv1= tk.Button(window, text="Izvēlēties",command=partial(frizieri_spec,bnoskusana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.2)
  izv2= tk.Button(window, text="Izvēlēties",command=partial(frizieri_spec,bapgriesana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.3)
  izv3= tk.Button(window, text="Izvēlēties",command=partial(frizieri_spec,bkrasošana),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.4)
  atpakal=tk.Button(window, text="< Atpakaļ",command=frizieri,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9)

def frizieri():
  for widgets in window.winfo_children():
        widgets.destroy()
  tips=tk.Label(window, text="Izvēlieties pakalpojuma veidu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  sieviesu = tk.Button(window, text="Sieviešu",command=s_pakal,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.2)
  viriesu= tk.Button(window, text="Vīriešu",command=v_pakal,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.3)
  bernu= tk.Button(window, text="Bērnu",command=b_pakal,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.4)
  atpakal=tk.Button(window, text="< Atpakaļ",command=clicked,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9)

def masaza():
  for widgets in window.winfo_children():
        widgets.destroy()
  mmedus="Medus masāža"
  mspeka="Spēka masāža"
  msokolades="Šokolādes masaža"
  tips=tk.Label(window, text="Izvēlieties pakalpojuma tipu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  medus=tk.Label(window, text="Medus masāža- 20€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.05,rely=0.2)
  speka=tk.Label(window, text="Spēka masāža- 25€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.05,rely=0.3)
  sokolades=tk.Label(window, text="Šokolādes masāža- 35€",bg='#262626',fg='#FFFFFF',font=('Calibri',11)).place(anchor="w",relx=0.05,rely=0.4)
  izv1 = tk.Button(window, text="Izvēlēties",command=partial (masieri_spec,mmedus),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.2)
  izv2= tk.Button(window, text="Izvēlēties",command=partial (masieri_spec,mspeka),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.3)
  izv3= tk.Button(window, text="Izvēlēties",command=partial (masieri_spec,msokolades),width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.8,rely=0.4)
  text=tk.Button(window,text="< Atpakaļ",command=clicked,width=7,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.15,rely=0.9)

def clicked():
  for widgets in window.winfo_children():
        widgets.destroy()
  pakalpojumi = tk.Label(text="Izvēlieties pakalpojumu",bg='#262626',fg='#ccffa6',font=('Calibri',12)).place(anchor="c",relx=0.5,rely=0.1)
  frizieris = tk.Button(window, text="Frizieris",command=frizieri,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.2)
  masieris= tk.Button(window, text="Masieris",command=masaza,width=10,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.3)
  

hello = tk.Label(text="Sveicināti!",bg='#262626',fg='#ccffa6',font=('Calibri',14)).place(anchor="c",relx=0.5,rely=0.1)
hello1 = tk.Label(text="Mūsu salona darba laiks ir Pr.- Sv. 8:00-18:00",bg='#262626',fg='#ccffa6',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.16)
button = tk.Button(window, text="Veikt pierakstu",command=clicked,bg='#262626',fg='#FFFFFF',highlightthickness=0,activebackground='#3d3737',activeforeground='#737373',font=('Calibri',11)).place(anchor="c",relx=0.5,rely=0.25)
tk.mainloop()