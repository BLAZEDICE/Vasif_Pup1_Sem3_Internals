from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("1305x652")
root.config(background="royalblue")

def theme():
    frame1.config(background="yellow")
    root.config(background="Pink")
    lab1.config(background="Pink")
    lab2.config(background="Pink")
    lab3.config(background="Yellow")
    garb_lab.config(background="Pink")


def insert():
    my_first_name=first_name_val.get()
    my_last_name=last_name_val.get()
    my_gend=gender_val.get()
    myemail=email_val.get()
    myzip=zip_val.get()

    if my_first_name.isnumeric():
        messagebox.showerror("Error","No digits are allowed")
    else:
        lb1.insert(0,my_first_name)
    
    if my_last_name.isnumeric():
        messagebox.showerror("Error","No digits are allowed")
    else:
        lb1.insert(1,my_last_name)

    lb1.insert(2,my_gend)
    lb1.insert(3,myemail)
    
    if(myzip).isnumeric():
        lb1.insert(4,myzip)
    else:
        messagebox.showerror("Error","Digits required")

   

def delete():
    lb1.delete(ANCHOR)
   
lab1=Label(root,text="              ",background="royalblue")
lab1.grid(row=0,column=0)

frame1=Frame(root,border=3,width=450,height=520)
frame1.config(highlightbackground="black",highlightthickness=4)
frame1.grid(row=1,column=1,rowspan=3)

garb_lab=Label(root,text="              ",background="royalblue")
garb_lab.grid(row=0,column=2)
insert_but=Button(root,text="Insert",command=insert).grid(row=1,column=3)
delete_but=Button(root,text="Delete",command=delete).grid(row=2,column=3)
theme_but=Button(root,text="Theme",command=theme).grid(row=3,column=3)

lab2=Label(root,text="              ",background="royalblue")
lab2.grid(row=0,column=4)

frame2=Frame(root,border=3,width=450,height=520)
frame2.config(highlightbackground="black",highlightthickness=4)
frame2.grid(row=1,column=5,rowspan=5)
frame1.grid_propagate("False")
frame2.grid_propagate("False")

first_name_lab=Label(frame1,text="First Name:",font="Arial 10 bold").grid(row=0,column=0)
first_name_val=StringVar()
lab3=Label(frame1,text="              ")
lab3.grid(row=0,column=1,columnspan=2)
first_name_inp=Entry(frame1,textvariable=first_name_val,width=25).grid(row=0,column=3)

last_name_lab=Label(frame1,text="Last Name:",font="Arial 10 bold").grid(row=1,column=0)
last_name_val=StringVar()
last_name_inp=Entry(frame1,textvariable=last_name_val,width=25).grid(row=1,column=3)

gender_val=StringVar()
gender_lab=Label(frame1,text="Gender:",font="Arial 10 bold").grid(row=2,column=0)

male_rad=Radiobutton(frame1,text="Male",variable=gender_val).grid(row=2,column=2)
female_rad=Radiobutton(frame1,text="Female",variable=gender_val).grid(row=2,column=3)

gender_lab=Label(frame1,text="Languages:",font="Arial 10 bold").grid(row=3,column=0)

telugu_val=IntVar()
telugu_but=Checkbutton(frame1,text="Telugu",variable=telugu_val,onvalue=1,offvalue=0,height=2,width=10).grid(row=3,column=2)

english_val=IntVar()
english_but=Checkbutton(frame1,text="English",variable=english_val,onvalue=1,offvalue=0,height=2,width=10).grid(row=3,column=3)

hindi_val=IntVar()
hindi_but=Checkbutton(frame1,text="Hindi",variable=hindi_val,onvalue=1,offvalue=0,height=2,width=10).grid(row=3,column=4)

email_lab=Label(frame1,text="Email:",font="Arial 10 bold").grid(row=4,column=0)
email_val=StringVar()
email_inp=Entry(frame1,textvariable=email_val,width=25).grid(row=4,column=3)

add_scroll=Scrollbar(frame1)
add_scroll.grid(row=5,column=4)
add_lab=Label(frame1,text="Address:",font="Arial 10 bold").grid(row=5,column=0)
add_inp=Text(frame1,width=25,height=10,yscrollcommand=add_scroll.set)
add_scroll.config(command=add_inp.yview)
add_inp.grid(row=5,column=3)

state_lab=Label(frame1,text="State:",font="Arial 10 bold").grid(row=6,column=0)
state_val=StringVar()
state_menu=OptionMenu(frame1,variable=state_val,value="Mumbai")
state_menu.grid(row=6,column=3)

zip_lab=Label(frame1,text="Zip:",font="Arial 10 bold").grid(row=7,column=0)
zip_val=StringVar()
zip_inp=Entry(frame1,textvariable=zip_val,width=25)
zip_inp.grid(row=7,column=3)

zip_lab=Label(frame1,text="Credit Card Type:",font="Arial 10 bold").grid(row=8,column=0)
cred_card_val=StringVar()
crad_card_menu=OptionMenu(frame1,variable=state_val,value="HDFC")
crad_card_menu.grid(row=8,column=3)

billing_rec_lab=Label(frame2,text="Billing Records",background="gray",padx=145,font="Arial 15 bold").grid(row=0,column=0)
lb1=Listbox(frame2,width=70,height=29)
lb1.grid(row=1,column=0)
root.mainloop()