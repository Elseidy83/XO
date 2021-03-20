import random
from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import ImageTk
import time

root = Tk()
d_img = ImageTk.PhotoImage(file="d.png")
x_img = ImageTk.PhotoImage(file="x.jpg")
o_img = ImageTk.PhotoImage(file="o.png")
# result ={str(i):i for i in range(1,10)}
# result ={str(x)+str(c):'' for x in range(3) for c in range(3)}
result ={str(x):f'{x}' for x in range(1,10) }

l_x = 1
# [(x,c)  for x in range(1,1000) for c in range (x,1000) if x*c==300]
l_btns=[]
def main(height=5,width=5):
    print(result)
    l_i = 1
    globals()['l_btns']=[]
    for x in range(width):
        for y in range(height):
          btn = tkinter.Button(root,text=str(l_i),width=170,height=170,image=d_img)
          result[str(l_i)]=str(l_i)
          l_i+=1
          btn.grid(column=x, row=y, sticky=N+S+E+W)
          # btn["command"] = lambda btn=btn: click(btn)
          btn["command"] = lambda btn=btn: make_selection(btn)
          l_btns.append(btn)
    print(result)
def make_selection(button):
    print(button["text"])
    if l_x%2 == 0 and button["image"] == 'pyimage1':
        button["image"] = o_img
        result[button['text']] = 'o_img'
        globals()['l_x'] += 1
    elif button["image"] == 'pyimage1':
        button["image"] = x_img
        result[button['text']] = 'x_img'
        globals()['l_x'] += 1
    print(result)
    who_is_winner(result)
    take_action(l_x%2 == 0)

def take_action(user_2):
    time.sleep(0.25)
    if user_2:
        l_rand = random.randint(0,8)
        print(l_rand)
        print('no of btns '+str(len(l_btns)))
        # l_btns[random.randint(0,9)]
        make_selection(l_btns[l_rand])

def who_is_winner(result):
    if (result['1']==result['4']==result['7']) or (result['1']==result['2']==result['3']) or (result['1']==result['5']==result['9']):
        messagebox.showinfo("Hello", result['1'] +" Is the winner")
        main(3,3)
        # root.quit()
    if (result['2']==result['5']==result['8']):
        messagebox.showinfo("Hello", result['2'] +" Is the winner")
        main(3, 3)
        # root.quit()
    if (result['3']==result['6']==result['9']):
        messagebox.showinfo("Hello", result['3'] +" Is the winner")
        main(3, 3)
        # root.quit()
    if (result['4']==result['5']==result['6']):
        messagebox.showinfo("Hello", result['4'] +" Is the winner")
        main(3, 3)
        # root.quit()
    if (result['7']==result['8']==result['9']) or (result['7']==result['5']==result['3']):
        messagebox.showinfo("Hello", result['7'] +" Is the winner")
        # root.quit()
        main(3, 3)
w= main(3,3)
tkinter.mainloop()