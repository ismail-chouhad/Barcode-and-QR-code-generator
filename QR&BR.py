########### COMMAND ############
#pip install qrcode
#pip isntall pillow
#pip install python-barcode
################################

#!!!!! Check the path of the images, if it is not displayed !!!!!!!

from tkinter import *
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import  Image, ImageTk

class window:
    
    def __init__(self,wind):
        self.wind=wind
        wind.geometry("900x500+200+100")
        wind.title("Le générateur de QR code & barre code v(1.0)")
        wind.resizable(False,False)
        wind.config(bg='#FFFFFF')
        
        header=Label(wind,text='Le générateur de barre code & QR code',font=('Verdana',20,'bold'),
                       fg="white",bg='#f24f24',anchor='n')
        
        frmsidew=Frame(wind,bg='lightgray',relief=RIDGE,bd=2)
        frmsidee=Frame(wind,bg='lightgray',relief=RIDGE,bd=2)
        
        txtsidew=Label(frmsidew,text='Code QR',font=('Verdana',21,'bold'),
                       fg="white",bg='#f24f24',anchor='n')
        txtsidee=Label(frmsidee,text='Code Barre',font=('Verdana',20,'bold'),
                       fg="white",bg='#f24f24',anchor='n')
        
        imgQR=Image.open('C:/Users/DELL/Desktop/ProjetQR&BR/QRandBR/QRimage.png')
        resized_imgQR=imgQR.resize((370,370))
        QR_image=ImageTk.PhotoImage(resized_imgQR)
        
        btnQR=Button(frmsidew,command=QRcode.qrfct,
                     image=QR_image,relief=GROOVE,bd=4,cursor="hand2")

        imgBR=Image.open('C:/Users/DELL/Desktop/ProjetQR&BR/QRandBR/BRimage.png')
        resized_imgBR=imgBR.resize((480,600))
        BR_image=ImageTk.PhotoImage(resized_imgBR)
        
        btnBR=Button(frmsidee,command=BRcode.brfct,
                     relief=GROOVE,bd=4,cursor="hand2",image=BR_image)
        
        #Positions
        header.place(x=0,y=0,relwidth=1.01)
        frmsidew.place(x=20,y=70,height=400,width=420)
        frmsidee.place(x=460,y=70,height=400,width=420)
        txtsidew.place(x=0,y=0,relwidth=1.01)
        txtsidee.place(x=0,y=0,relwidth=1.01)
        btnQR.place(x=40,y=55,height=330,width=330)
        btnBR.place(x=25,y=100,height=230,width=370)
        
        wind.mainloop()

class QRcode:
    
    def __init__(self,rootQR):
        self.rootQR=rootQR
        rootQR.geometry("900x500+200+100")
        rootQR.title("Code QR")
        rootQR.resizable(False,False)
        
        headerqr=Label(rootQR,text='Le générateur de code QR',font=('Verdana',20,'bold'),
                       fg="white",bg='#f24b24',anchor='n')
        
        frmsidew=Frame(rootQR,bg='white',relief=RIDGE,bd=2)
        frmsidee=Frame(rootQR,bg='white',relief=RIDGE,bd=2)
        
        txtsidew=Label(frmsidew,text='Les informations de produit',font=('Verdana',21,'bold'),
                       fg="white",bg='#f24b24',anchor='n')
        txtsidee=Label(frmsidee,text='Code QR',font=('Verdana',20,'bold'),
                       fg="white",bg='#f24b24',anchor='n')

        self.qr_code=Label(frmsidee,text="Pas de code QR\n disponible",font=('Verdana',10),
                           fg="black",bg='lightgray',relief=GROOVE,bd=4)
        
    
        self.var_id=StringVar()
        self.var_n=StringVar()
        self.var_fb=StringVar()
        self.var_p=StringVar()
        self.var_dp=StringVar()
        self.var_de=StringVar()
        
        lbl_id=Label(frmsidew,text="ID",font=('Verdana',15),bg='white')
        lbl_n=Label(frmsidew,text="Nom ",font=('Verdana',15),bg='white')
        lbl_fb=Label(frmsidew,text="Fabricant",font=('Verdana',15),bg='white')
        lbl_p=Label(frmsidew,text="Poids",font=('Verdana',15),bg='white')
        lbl_dp=Label(frmsidew,text="Date de production",font=('Verdana',15),bg='white')
        lbl_de=Label(frmsidew,text="Date d'expiration",font=('Verdana',15),bg='white')


        entry_id=Entry(frmsidew,textvariable=self.var_id,font=('Verdana',15),bg='lightyellow')
        entry_n=Entry(frmsidew,textvariable=self.var_n,font=('Verdana',15),bg='lightyellow')
        entry_fb=Entry(frmsidew,textvariable=self.var_fb,font=('Verdana',15),bg='lightyellow')
        entry_p=Entry(frmsidew,textvariable=self.var_p,font=('Verdana',15),bg='lightyellow')
        entry_dp=Entry(frmsidew,textvariable=self.var_dp,font=('Verdana',15),bg='lightyellow')
        entry_de=Entry(frmsidew,textvariable=self.var_de,font=('Verdana',15),bg='lightyellow')

        btng=Button(frmsidee,text="Générer",font=('Verdana',15,'bold'),fg="black",command=self.generer,
                     bg='#1eeaa1',relief=GROOVE,bd=2,cursor="hand2")
        btne=Button(frmsidee,text="Effacer",font=('Verdana',15,'bold'),fg="black",command=self.effacer,
                     bg='red',relief=GROOVE,bd=2,cursor="hand2")
        
        self.msg=""
        self.lblmsg=Label(frmsidee,text=self.msg,fg="green",bg="white",font=('Verdana',9,'bold'))

        #Positions
        headerqr.place(x=0,y=0,relwidth=1.01)
        frmsidew.place(x=20,y=70,height=400,width=588)
        frmsidee.place(x=630,y=70,height=400,width=252)
        txtsidew.place(x=0,y=0,relwidth=1.01)
        txtsidee.place(x=0,y=0,relwidth=1.01)
        self.qr_code.place(x=5.5,y=40,height=240,width=240)
        lbl_id.place(x=10,y=50)
        lbl_n.place(x=10,y=110)
        lbl_fb.place(x=10,y=170)
        lbl_p.place(x=10,y=230)
        lbl_dp.place(x=10,y=290)
        lbl_de.place(x=10,y=350)
        entry_id.place(x=240,y=50,height=30,width=330)
        entry_n.place(x=240,y=110,height=30,width=330)
        entry_fb.place(x=240,y=170,height=30,width=330)
        entry_p.place(x=240,y=230,height=30,width=330)
        entry_dp.place(x=240,y=290,height=30,width=330)
        entry_de.place(x=240,y=350,height=30,width=330)
        btng.place(x=0,y=310,relwidth=1.01)
        btne.place(x=0,y=353,relwidth=1.01)
        self.lblmsg.place(x=0,y=283,relwidth=1)

    def effacer(self):
        self.var_id.set('')
        self.var_n.set('')
        self.var_fb.set('')
        self.var_p.set('')
        self.var_dp.set('')
        self.var_de.set('')
        self.msg=''
        self.lblmsg.config(text=self.msg)
        self.qr_code.config(image='')
        
    def generer(self):
        if self.var_id.get()=="" or self.var_n.get()=="" or self.var_fb.get()=="" or self.var_p.get()=="" or self.var_dp.get()=="" or self.var_de.get()=="":
            self.msg='Tous les champs sont obligatoires !'
            self.lblmsg.config(text=self.msg,fg='red')
            
        else:
            self.msg='Le code QR généré avec succès :)'
            self.lblmsg.config(text=self.msg,fg='green')
            
            #########qrcode###########
#("Les informations de produit sont : \n ID : {}\n Nom : {}\n Fabricant : {}\n Poids : {}\n Date de prodiction : {}\n Date d'expiration : {}\n").format(self.var_id.get(), self.var_n.get(),self.var_fb.get(),self.var_p.get(),self.var_dp.get(),self.var_de.get())
#f"Les informations de produit sont : \n ID : {self.var_id.get()}\n Nom : {self.var_n.get()}\n Fabricant : {self.var_fb.get()}\n Poids : {self.var_p.get()}\n Date de prodiction : {self.var_dp.get()}\n Date d'expiration : {self.var_de.get()}\n"
            QR_data=("Les informations de produit sont : \n ID : {}\n Nom : {}\n Fabricant : {}\n Poids : {}\n Date de prodiction : {}\n Date d'expiration : {}\n").format(self.var_id.get(), self.var_n.get(),self.var_fb.get(),self.var_p.get(),self.var_dp.get(),self.var_de.get())
            QR_code=qrcode.make(QR_data)
            QR_code.save('C:/Users/DELL/Desktop/ProjetQR&BR/QRandBR/QR/ID_'+str(self.var_id.get())+'.png')
            QR_code=QR_code.resize((240,240))
            ########PILLOW#############
            self.im=ImageTk.PhotoImage(QR_code)
            self.qr_code.config(image=self.im)
                
    def qrfct():
        wind.destroy()
        rootQR=Tk()
        QRcode(rootQR)
        rootQR.mainloop()
        
class BRcode:
    
    def __init__(self,rootBR):
        self.rootBR=rootBR
        rootBR.geometry("900x500+200+100")
        rootBR.title("Code Barre")
        rootBR.resizable(False,False)
        
        headerbr=Label(rootBR,text='Le générateur de code Barre',font=('Verdana',20,'bold'),
                       fg="white",bg='#f24b24',)

        frmcenter=Frame(rootBR,bg='white',relief=RIDGE,bd=2)
        frmsouth=Frame(rootBR,bg='white',relief=RIDGE,bd=2)

        txtcenter=Label(frmcenter,text=' Le Numéro de produit',font=('Verdana',21,'bold'),
                       fg="white",bg='#f24b24')
        txtsouth=Label(frmsouth,text='Code Barre',font=('Verdana',20,'bold'),
                       fg="white",bg='#f24b24')

        self.br_code=Label(frmsouth,text="Pas de code Barre\n disponible",font=('Verdana',10),
                           fg="black",bg='lightgray',relief=GROOVE,bd=4)

        self.var_N=StringVar()

        lbl_N=Label(frmcenter,text=" N °  ",font=('Verdana',25),bg='white')
        entry_N=Entry(frmcenter,relief=GROOVE,bd=3,textvariable=self.var_N,font=('Verdana',25),bg='lightyellow')

        btng=Button(frmsouth,text="Générer",font=('Verdana',20,'bold'),fg="black",command=self.generer,
                     bg='#1eeaa1',relief=GROOVE,bd=2,cursor="hand2")
        btne=Button(frmsouth,text="Effacer",font=('Verdana',20,'bold'),fg="black",command=self.effacer,
                     bg='red',relief=GROOVE,bd=2,cursor="hand2")

        self.msg=""
        self.lblmsg=Label(frmcenter,text=self.msg,fg="green",bg="white",font=('Verdana',12,'bold'))

        #Positions
        headerbr.place(x=0,y=0,relwidth=1.01)
        frmcenter.place(x=20,y=55,height=150,width=855)
        frmsouth.place(x=120,y=225,height=250,width=655)
        txtcenter.place(x=0,y=0,relwidth=1.01)
        txtsouth.place(x=0,y=0,relwidth=1.01)
        self.br_code.place(x=10,y=44,height=200,width=422)
        lbl_N.place(x=50,y=50)
        entry_N.place(x=155,y=50,height=50,width=625)
        btng.place(x=444,y=44,height=100,width=200)
        btne.place(x=444,y=142,height=100,width=200)
        self.lblmsg.place(x=0,y=110,relwidth=1)
        
    def effacer(self):
        self.var_N.set("")
        self.msg=""
        self.lblmsg.config(text=self.msg)
        self.br_code.config(image="")
        
    def generer(self):
        if  self.var_N.get()=="":
            self.msg='Le Numéro de produit est obligatoire !'
            self.lblmsg.config(text=self.msg,fg='red')
            
        elif len(self.var_N.get())!=13 :
            self.msg='SVP entrer 13 nombres entiers !'
            self.lblmsg.config(text=self.msg,fg='red')
            
        else:
            self.msg='Le code Barre généré avec succès :)'
            self.lblmsg.config(text=self.msg,fg='green')
            Br_code= EAN13(self.var_N.get(),writer=ImageWriter())
            Br_path='C:/Users/DELL/Desktop/ProjetQR&BR/QRandBR/BR/N°'+str(self.var_N.get())
            Br_img=Br_code.save(Br_path)
            imgBR=Image.open(Br_img)
            resized_imgBR=imgBR.resize((550,500))
            self.BR_image=ImageTk.PhotoImage(resized_imgBR)
            self.br_code.config(image=self.BR_image)
  
    def brfct():
        wind.destroy()
        rootBR=Tk()
        BRcode(rootBR)
        rootBR.mainloop()   

wind=Tk()
window(wind)


