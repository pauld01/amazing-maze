from tkinter import*
from timeit import default_timer

fenêtre = Tk()
can=Canvas(fenêtre,bg="white",height=100,width=150)
can.pack()

def chronomètre():
    now = default_timer() - début
    minutes,secondes = divmod (now, 60)
    heures,minutes = divmod(minutes,60)
    str_time = "%d:%02d:%02d"%(heures,minutes,secondes)
    can.itemconfigure(text_clock, text=str_time)
    fenêtre.after(1000, chronomètre)

début = default_timer()
text_clock = can.create_text(65,25)

chronomètre()
fenêtre.mainloop()