import tkinter as tk


#Create window obj
window = tk.Tk()
# define 4 labels Title, Author, Year, ISBN
l1 = tk.Label(window, 
    text="The thankunext Translator!",
    fg = "pink",
    font="Helvetica 24 bold"
)
l2 = tk.Label(window, 
    text ="\n\nThis is a special translator. It will help you encode messages you you can secretly send them to your friends, publicly. Whaaat?",
    font="Helvetica 14")
l1.pack()
l2.pack()
#l1.grid(row=0, column=0)



window.mainloop()