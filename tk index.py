
from tkinter import *
from dictionaries import *


windows = Tk()
windows.geometry("300x300")
windows.title("MEXICAN DICTIONARY")


entry_text = Entry(windows)
entry_text.pack()

result = StringVar()
result_label = Label(windows, textvariable=result)
result_label.pack()



def check(word):
        if word in ebira_dictionary:
            result.set(ebira_dictionary[word])
            print(ebira_dictionary[word])

        else:
            result.set("Not found")
            print("Not found")


ebira_button = Button(windows)
ebira_button.config(text='check', command=lambda : check(entry_text.get().lower()))
ebira_button.pack()
windows.mainloop()

windows.mainloop()