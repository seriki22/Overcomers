
from tkinter import *
from dictionaries import ebira_dictionary


windows3 = Tk()
windows3.geometry("300x300")
windows3.title("MEXICAN DICTIONARY")


entry_text = Entry(windows3)
entry_text.pack()

result = StringVar()
result_label = Label(windows3, textvariable=result)
result_label.pack()



def check(word):
        if word in ebira_dictionary:
            result.set(ebira_dictionary[word])
            print(ebira_dictionary[word])

        else:
            result.set("Not found")
            print("Not found")


ebira_button = Button(windows3)
ebira_button.config(text='check', command=lambda : check(entry_text.get().lower()))
ebira_button.pack()
windows3.mainloop()

windows3.mainloop()