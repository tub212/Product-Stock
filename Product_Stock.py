from Tkinter import *
from stock  import *
#import tkFont
#Git-HUB
#helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")

def fun(xxx):
    return len(xxx[0])

def maxlist():
    return len(max(product_stock, key = fun)[0])

print maxlist()

def writedata():
    f = open("phone.py", "w")
    f.write("product_stock = " + str(product_stock))
    f.close()
    
def whichSelected () :
    print product_stock[select.curselection()[0]][0]
    print "At %s of %d" % (select.curselection(), len(product_stock))
    print nameVar.get()
    return int(select.curselection()[0])

def addEntry () :
    product_stock.append ([nameVar.get(), phoneVar.get()])
    setSelect ()
    writedata()

def updateEntry() :
    product_stock[whichSelected()] = [nameVar.get(), phoneVar.get()]
    setSelect ()
    writedata()

def deleteEntry() :
    del product_stock[whichSelected()]
    setSelect ()
    writedata()

def loadEntry  () :
    name, phone = product_stock[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)

def makeWindow () :
    global nameVar, phoneVar, select
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)
    

    Label(frame1, text="Phone").grid(row=1, column=0, sticky=W)
    phoneVar= StringVar()
    phone= Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    b2 = Button(frame2,text="Update",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Load ",command=loadEntry)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=10, width=100)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    return win

def setSelect () :
    space = maxlist()
    product_stock.sort()
    select.delete(0,END)
    for name,phone in product_stock :
        select.insert (END, name + ' '*(space - len(name))+' |')
        #print (END, name)

win = makeWindow()
setSelect ()
win.mainloop()
