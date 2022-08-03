from tkinter import *
from tkinter import messagebox, simpledialog

current_page_index = 0

root = Tk()

root.title("学习日语: あいうえお　うた")  # 学习日语 = Learn Japanese
root.geometry("1000x618")
root.resizable(0, 0)
root.config(background="#999999")

title = Label(master=root, text="あいうえお　うた", font=("Helvetica", 20), background="#999999")  # Title
title.place(x=0, y=0)

learning_word_index = 0
learning_word_list = ["ありのこ　あちこち", "いしころ　いろいろ", "うしさん　うとうと", "えんそく　えいえい", 'おひさま　おてんき']  # word list(Page list)


def index_minus():
    global learning_word_index
    if learning_word_index > 0:
        learning_word_index -= 1
        print(learning_word_index)
    Current_learning_word["text"] = learning_word_list[learning_word_index]


def index_plus():
    global learning_word_index, Current_learning_word
    if learning_word_index < 4:
        learning_word_index += 1
        print(learning_word_index)
    Current_learning_word["text"] = learning_word_list[learning_word_index]
    root.update()


Current_learning_word = Label(master=root, text=learning_word_list[learning_word_index], font=("Helvetica", 50),
                              background="#999999")
Current_learning_word.place(x=200, y=50)
Local_learning_word = Label(master=root, text="あいうえお", font=("Helvetica", 50), background="#999999")  # Title
Local_learning_word.place(x=200, y=150)
Index_next_button = Button(root, text="下一句", command=index_plus)  # 下一句=Next line
Index_next_button.place(x=215, y=400)
Index_next_button.configure(height=2, width=12)
Index_before_button = Button(root, text="上一句", command=index_minus)  # 上一句=Last line
Index_before_button.place(x=720, y=400)
Index_before_button.configure(height=2, width=12)


root.mainloop()
