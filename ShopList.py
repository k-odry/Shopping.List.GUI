import pickle
from tkinter import *
import os

"""Shopping List Application with GUI - Created by Karoly Odry | 24/07/2020"""

frame = Tk()
# frame.attributes("-alpha", 0.9) # ---> set opacity of frame
frame.title('Shopping List - by Karoly Odry')
frame.geometry('324x600+200+80')
frame.iconbitmap("C:\\Users\\k\\PycharmProjects\\untitled\\ShopList\\bb_32x32.ico")
frame.resizable(width=False, height=False)

c = Canvas(frame, height=600, width=300)
image = PhotoImage(file='C:\\Users\\k\\PycharmProjects\\untitled\\ShopList\\notepaper_bg.png')
bg_label = Label(frame, image=image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
c.place(x=0, y=0)

font = ('Helvetica', 9, 'bold')
entries = []
chb_list = []  # ---> new
var = dict()
filename = "entries.txt"


def on_click(event):
    en.configure(state=NORMAL)
    en.delete(0, END)

    # callback to only work once
    en.unbind('<Button-1>', on_click_id)


def del_item(key):
    chb_list[key].destroy()


def add_entry(row=None):
    chb = chb_list
    e = str(en.get())
    en.delete(0, END)
    entries.append(e)
    entext.set('')
    n = len(chb)
    lb = Checkbutton(frame, text=e, variable=n, fg='#141951', bg='#ffffff', font=font, onvalue=1, offvalue=0,
                     command=lambda key=n: del_item(key))
    lb.grid(row=row, column=0, padx=5, pady=0.5, ipady=0, sticky=NW)
    chb.append(lb)  # ---> new


def save_list():
    file = open(filename, 'wb')
    pickle.dump(entries, file)
    update_btn_state_on()

def update_btn_state_on():
    load_btn.config(state=NORMAL)
    return load_btn


def update_btn_state_off():
    # load_btn.config(fg='red')
    load_btn.config(state=DISABLED)
    return load_btn


def open_list(row=None):
    file = open(filename, 'rb')

    if os.stat('entries.txt').st_size == 0:
        update_btn_state_off()
    else:
        new_entries = pickle.load(file)
        entries.append(new_entries)

        for index, elem in enumerate(new_entries):
            elem.strip()
            var[index] = IntVar()
            lb = Checkbutton(frame, text=elem, variable=var[index], fg='#141951', bg='#ffffff', font=font, onvalue=1,
                             offvalue=0,
                             command=lambda key=index: del_item(key))
            lb.grid(row=row, column=0, padx=5, pady=0.5, ipady=0, sticky=NW)
            chb_list.append(lb)


entext = StringVar()
en = Entry(frame, textvariable=entext, fg='#141951', bg='#e6dcb8', bd=4, relief='ridge', font=font)
en.insert(0, "Click to Enter Item")
en.configure(state=DISABLED)
on_click_id = en.bind('<Button-1>', on_click)
en.grid(row=0, column=0, ipadx=7, ipady=1, padx=7, pady=9)

add_btn = Button(frame, text='+', bg='#e6dcb8', relief='ridge', font=font, command=add_entry)
add_btn.grid(row=0, column=1, padx=7, pady=9)

save_btn = Button(frame, text='Save', bg='#e6dcb8', relief='ridge', font=font, command=save_list)
save_btn.grid(row=0, column=2, padx=7, pady=9)

load_btn = Button(frame, text='Load', bg='#e6dcb8', relief='ridge', font=font, command=open_list)
load_btn.grid(row=0, column=3, padx=7, pady=9)

frame.mainloop()
