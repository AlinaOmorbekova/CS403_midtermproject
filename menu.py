from tkinter import *
from tkinter import font


root = Tk()
root.geometry("1000x500")
root.title("Billing Management")
root.resizable(False, False)


def Reset():
    entry_mexican.delete(0, END)
    entry_veganhot.delete(0, END)
    entry_chickenhot.delete(0, END)
    entry_pepperonifresh.delete(0, END)
    entry_doublepepperoni.delete(0, END)
    entry_hawaiian.delete(0, END)

def Total():
    try: a1 = int(mexican.get())
    except: a1 = 0  
    try: a2 = int(vegan_hot.get())
    except: a2 = 0
    try: a3 = int(chicken_hot.get())
    except: a3 = 0
    try: a4 = int(pepperoni_fresh.get())
    except: a4 = 0
    try: a5 = int(double_pepperoni.get())
    except: a5 = 0
    try: a6 = int(hawaiian.get())
    except: a6 = 0  

    #define cost of each item
    c1 = 520 * a1    
    c2 = 390 * a2
    c3 = 395 * a3
    c4 = 395 * a4
    c5 = 475 * a5
    c6 = 365 * a6

    lbl_total = Label(f2, font=('aria', 20, 'bold'), text='Total', width=16, fg='lightyellow', bg='black')
    lbl_total.place(x=0, y=50)

    entry_total = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6, width=15, bg='lightgreen')
    entry_total.place(x=20, y=100)

    totalcost = c1+c2+c3+c4+c5+c6
    string_bill = "Sum:", str(totalcost)
    Total_bill.set(string_bill)

Label( text="BILL MANAGEMENT for Pizzeria", bg='black', fg='white', font=("calibri", 33), width="300", height="2").pack()

#Menu card
f = Frame(root, bg='lightgreen', highlightbackground='black', highlightthickness=1, width=310, height=370)
f.place(x=10, y=118)

Label(f, text="Menu", font=('Gabriola', 40, "bold"), fg='black', bg='lightgreen').place(x=80, y=0)

Label(f, font=("Lucia Calligraphy", 15, "bold"), text="Mexican pizza .... 520 som", fg='black', bg="lightgreen").place(x=10, y=80)
Label(f, font=("Lucia Calligraphy", 15, "bold"), text="Vegan Hot .... 390 som", fg='black', bg="lightgreen").place(x=10, y=110)
Label(f, font=("Lucia Calligraphy", 15, "bold"), text="Chicken Hot .... 395 som", fg='black', bg="lightgreen").place(x=10, y=140)
Label(f, font=("Lucia Calligraphy", 15, "bold"), text="Pepperoni Fresh .... 395 som", fg='black', bg="lightgreen").place(x=10, y=170)
Label(f, font=("Lucia Calligraphy", 15, "bold"), text="Double Pepperoni .... 475 som", fg='black', bg="lightgreen").place(x=10, y=200)
Label(f, font=("Lucia Calligraphy", 15, "bold"), text="Hawaiian .... 365 som", fg='black', bg="lightgreen").place(x=10, y=230)

#Bill
f2 = Frame(root, bg='lightyellow', highlightbackground='black', highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)

Bill = Label(f2,text='Bill', font=('calibri', 20), bg='lightyellow')
Bill.place(x = 120, y = 10)


#Entry work
f1 = Frame(root, bd=5, height=370, width=300,relief=RAISED)
f1.pack()


mexican = StringVar()
vegan_hot = StringVar()
chicken_hot = StringVar()
pepperoni_fresh = StringVar()
double_pepperoni = StringVar()
hawaiian = StringVar()
Total_bill = StringVar()

#Label
lbl_mexican = Label(f1, font=("aria", 16, 'bold'), text = 'Mexican', width = 15, fg='blue4')
lbl_mexican.grid(row=1, column=0)
lbl_veganhot = Label(f1, font=("aria", 16, 'bold'), text = 'Vegan Hot', width = 15, fg='blue4')
lbl_veganhot.grid(row=2, column=0)
lbl_chickenhot = Label(f1, font=("aria", 16, 'bold'), text = 'Chicken Hot', width = 15, fg='blue4')
lbl_chickenhot.grid(row=3, column=0)
lbl_pepperonifresh = Label(f1, font=("aria", 16, 'bold'), text = 'Pepperoni fresh', width = 15, fg='blue4')
lbl_pepperonifresh.grid(row=4, column=0)
lbl_doublepepperoni = Label(f1, font=("aria", 16, 'bold'), text = 'Double pepperoni', width = 15, fg='blue4')
lbl_doublepepperoni.grid(row=5, column=0)
lbl_hawaiian = Label(f1, font=("aria", 16, 'bold'), text = 'Hawaiian', width = 15, fg='blue4')
lbl_hawaiian.grid(row=6, column=0)

#Entry
entry_mexican = Entry(f1, font=("aria", 20,'bold'), textvariable=mexican, bd=6, width=8, bg='lightpink')
entry_mexican.grid(row=1, column=1)
entry_veganhot = Entry(f1, font=("aria", 20,'bold'), textvariable=vegan_hot, bd=6, width=8, bg='lightpink')
entry_veganhot.grid(row=2, column=1)
entry_chickenhot = Entry(f1, font=("aria", 20,'bold'), textvariable=chicken_hot, bd=6, width=8, bg='lightpink')
entry_chickenhot.grid(row=3, column=1)
entry_pepperonifresh = Entry(f1, font=("aria", 20,'bold'), textvariable=pepperoni_fresh, bd=6, width=8, bg='lightpink')
entry_pepperonifresh.grid(row=4, column=1)
entry_doublepepperoni = Entry(f1, font=("aria", 20,'bold'), textvariable=double_pepperoni, bd=6, width=8, bg='lightpink')
entry_doublepepperoni.grid(row=5, column=1)
entry_hawaiian = Entry(f1, font=("aria", 20,'bold'), textvariable=hawaiian, bd=6, width=8, bg='lightpink')
entry_hawaiian.grid(row=6, column=1)

#buttons
btn_reset = Button(f1, bd=5, fg='black', bg='lightblue', font=('ariel', 16, 'bold'), width=10, text='Reset', command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f1, bd=5, fg='black', bg='lightblue', font=('ariel', 16, 'bold'), width=10, text='Total', command=Total)
btn_total.grid(row=8, column=1)

root.mainloop()