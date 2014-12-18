from Tkinter import *
from product  import *
#Git-HUB


def fun(xxx):
    return len(xxx[0])

def maxlist():
    return len(max(productlist, key = fun)[0])

#print maxlist()

def writedata():
    f = open("product.py", "w")
    f.write("productlist = " + str(productlist))
    f.close()
    
def whichSelected () :
    #print productlist[select.curselection()[0]][0]
    #print "At %s of %d" % (select.curselection(), len(productlist))
    #print nameVar.get()
    return int(select.curselection()[0])

def addEntry () :
    productlist.append ([nameVar.get(), priceVar.get(), productVar.get()])
    setSelect ()
    writedata()

def updateEntry() :
    productlist[whichSelected()] = [nameVar.get(), priceVar.get(), productVar.get()]
    setSelect ()
    writedata()

def deleteEntry() :
    del productlist[whichSelected()]
    setSelect ()
    writedata()

def loadEntry  () :
    name, price, product = productlist[whichSelected()]
    nameVar.set(name)
    priceVar.set(price)
    productVar.set(product)

def printEntry () :
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    print "X Product Name                Price     Quantity X"
    for i in productlist:
        print "X  " + i[0] + " " *(28 - len(i[0])) + i[1] + \
              " " * (10 - len(i[1])) + i[2] + " " * (7 - len(i[2])) + " X"
    print "X                                                X"
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def makeWindow () :
    global nameVar, priceVar, productVar, select
    win = Tk()
    win.wm_title("Product Stock")

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Product Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)
    

    Label(frame1, text="Price").grid(row=1, column=0, sticky=W)
    priceVar= StringVar()
    product= Entry(frame1, textvariable=priceVar)
    product.grid(row=1, column=1, sticky=W)
    
    Label(frame1, text="Quantity").grid(row=2, column=0, sticky=W)
    productVar= StringVar()
    product= Entry(frame1, textvariable=productVar)
    product.grid(row=2, column=1, sticky=W)

    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Add ",command=addEntry)
    b2 = Button(frame2,text="Update",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Load ",command=loadEntry)
    b5 = Button(frame2,text=" Print ",command=printEntry)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT) ;b5.pack(side=LEFT)

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
    productlist.sort()
    select.delete(0,END)
    for name,price,product in productlist :
        select.insert (END, name)
        #print (END, name)

win = makeWindow()
setSelect ()
win.mainloop()
