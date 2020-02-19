import sys
import tkinter


root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

def DeleteEntryValue(event):
  #エントリーの中身を削除
  EditBox.delete(0, tkinter.END)

#ラベル
Static1 = tkinter.Label(text=u'test')
Static1.pack()
#エントリー
EditBox = tkinter.Entry()
EditBox.pack()
value = EditBox.get()
#ボタン
Button = tkinter.Button(text=u'ボタンです')
Button.bind("<Button-1>",DeleteEntryValue) 
Button.pack()


root.mainloop()