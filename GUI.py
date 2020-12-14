from tkinter import *
from tkinter.ttk import *
import re
import extractTextToImage
import threading

window = Tk()

window.title("Web IMG Scan")
window.geometry('400x280')

title = Label(window, text="Web IMG Scan",
              font=("Arial Bold", 30))

title.grid(columnspan=3, pady=40, padx=50, sticky=N)

lblUrl = Label(window, text="Enter URL:")

lblUrl.grid(column=0, row=1, padx=25, sticky=W)

txtUrl = Entry(window, width=30)

txtUrl.grid(column=1, row=1, ipadx=30, pady=5)


lblWord = Label(window, text="Enter a Word:")

lblWord.grid(column=0, row=2, padx=25, sticky=W)

txtWord = Entry(window, width=30)

txtWord.grid(column=1, row=2, ipadx=30)

labelError = Label(window)
labelError.grid(column=1, row=3, ipadx=30, pady=10)


def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Ok", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def clicked():

    result = None
    url = txtUrl.get()
    word = txtWord.get()
    if re.search("^https?://", url) and len(word) > 0 and result is None:
        progressBar = Progressbar(window, length=50, mode="indeterminate")
        progressBar.grid(columnspan=2, row=3,  pady=10)
        progressBar.start(5)
        btn.configure(state='disabled')
        labelError.configure(text='')
        try:
            result = extractTextToImage(url, word)
        except Exception as err:
            labelError.configure(
                text='A unexpected error happens,try again.', foreground="red")
            btn.configure(state='normal')
            progressBar.destroy()
        if result:
            progressBar.destroy()

            popupmsg(result)
            btn.configure(state='normal')

    else:
        labelError.configure(
            text='Please, enter a valid URL.', foreground="red")

    print(f"Runtime of the program is {end - start}")


btn = Button(window, text="Search",
             command=lambda: threading.Thread(target=clicked).start())

btn.grid(columnspan=3, row=4, pady=20)


window.mainloop()
