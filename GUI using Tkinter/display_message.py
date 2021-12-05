import tkinter as tk

def show(event):
    val_msg = ent_msg.get()#value entered in entry widget
    print(val_msg)

#     # lbl_output["text"]=val_msg

    lbl_output = tk.Label(text=val_msg,bg="cyan")
    lbl_output.pack(padx=5,pady=5)

    

window = tk.Tk()

lbl_msg=tk.Label(text="Enter Message:", width=10,bg="green",fg="white")
#width=10 TEXT UNITS ZERO ->WIDTH OF ZERO, HEIGHT -> HEIGHT OF ZERO
lbl_msg.pack()
#  #TOP TO BOTTOM CENTER

ent_msg = tk.Entry(width=20,bg="blue",fg="white")
ent_msg.pack(padx=5,pady=5)
# lbl_msg.pack()


# btn_display =tk.Button(text="Display",command=show)
# btn_display.pack()

# # lbl_output=tk.Label(text="", width=10,bg="blue",fg="white")
# # lbl_output.pack()

btn_display =tk.Button(text="Display")
btn_display.bind("<Button-1>",show)
btn_display.pack(padx=10,pady=10)


window.mainloop()




def show():
    val_msg = ent_msg.get()
    print(val_msg)

    frame4=tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
    frame4.grid(row=2,column=0)
    lbl_output=tk.Label(master=frame4,text=val_msg, width=10,bg="blue",fg="white")
    lbl_output.pack()

window = tk.Tk()

window.title("GUI Example")

# window.geometry("200x200")

# frm1 = tk.Frame(master=window,width=100,height=200,bg="#A56CDF")
# # frm1.pack(side=tk.LEFT)
# frm1.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=10,pady=20)
# # tk.TOP
# # tk.BOTTOM
# # tk.LEFT
# # tk.RIGHT

# lbl_1 = tk.Label(master=frm1, text="label1",bg="green")
# lbl_1.pack(side=tk.LEFT,fill=tk.Y)


# frm2 = tk.Frame(master=window,bg="blue",relief=tk.SUNKEN,borderwidth=5)
# frm2.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=5,pady=5)

# lbl_2 = tk.Label(master=frm2, text="label2",bg="yellow")
# lbl_2.pack(side=tk.RIGHT,fill=tk.Y)
# lbl_2.place(x=10,y=30)

# txt_para = tk.Text(master=frm2,bg="#EEAA99")
# # txt_para.pack()
# txt_para.place(x=50,y=70)

# frm1.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=10,pady=10)
# lbl_1.pack(side=tk.RIGHT,fill=tk.Y)



frame1=tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3,bg="yellow",width=100,height=100)
window.rowconfigure(0,weight=1,minsize=50)
window.columnconfigure(0,weight=1,minsize=50)
# # tk.FLAT: Has no border effect (the default value).
# # tk.SUNKEN: Creates a sunken effect.
# # tk.RAISED: Creates a raised effect.
# # tk.GROOVE: Creates a grooved border effect.
# # tk.RIDGE: Creates a ridged effect.
frame1.grid(row=0,column=0)

lbl_msg=tk.Label(master=frame1,text="Enter Message:", width=10,bg="green",fg="white")
lbl_msg.pack()

frame2=tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
frame2.grid(row=0,column=1)
ent_msg = tk.Entry(master=frame2)
ent_msg.pack()

frame3=tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=3)
frame3.grid(row=1,column=0)
btn_display =tk.Button(master=frame3,text="Display",width=15,relief=tk.RAISED,borderwidth=3,bg="#EC456B",command=show)
btn_display.pack()


window.mainloop()