from tiknter import *
master =Tk()
def callback():
    print("you have click the button")
btn =Button (master, text= 'ok',command = callback)
btn.pack()
mainloop()