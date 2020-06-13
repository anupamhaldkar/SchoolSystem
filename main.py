from tkinter import *
root1=Tk()
root1.geometry('1770x1080')
root1.configure(background='brown')
root1.title('Launcher Screen')
img=PhotoImage(file='dfg.gif')
l=Label(root1,text='School Management System based on tkinter\n\n Name - Anupam Haldkar\nBatch - A1\nPhone Number - 7********5\nEmail - ahdev2020@outlook.com\n\n move your cursor to continue',font=("Bradley Hand ITC",20,"bold"),bg='cyan',fg='black')
l.place(x=660,y=260)
def fun(e):
    root1.destroy()
    import newproject_2
    root1.mainloop()
l=Label(root1,image=img)
l.bind('<Motion>',fun)
l.place(x=40,y=5)
root1.mainloop()
