import tkinter as tk
from PIL import Image,ImageTk

#database coding work here
dataname="1234"
datapassword="1234"
datauserId="Student"

#global variable
entered_data="empty"

store_username="empty"
store_val="empty"
store_password="empty"

#check functions
def valid_credentials(user_login):
    My_username,My_userpassword,My_userId=user_login
    if(My_username==dataname and My_userpassword==datapassword and My_userId==datauserId):
        global entered_data 
        l = list(user_login)
        entered_data=l.copy()
        return True
    else:
        return False

def callback(input):
    if input.isdigit():
        print(input)
        return True             
    elif input is "":
        print(input)
        return True
    else:
        print(input)
        return False

#First login frame
my_login_window=tk.Tk()
my_login_window.title("Login Window")

reg = my_login_window.register(callback)

#getting the width and height of screen
scr_width= my_login_window.winfo_screenwidth()
scr_height= my_login_window.winfo_screenheight()
my_login_window.geometry("%dx%d" % (scr_width,scr_height))

#maximum and minimum size of screen window
my_login_window.maxsize(scr_width,scr_height)
my_login_window.minsize(int(scr_width/2),int(scr_height/2))

#background login image
my_image1= Image.open("login_bg.png")
Myimage_w,Myimage_h=my_image1.size
bg_ratio=Myimage_w/Myimage_h

bg_image= my_image1.resize((int(3*bg_ratio*scr_height/4),int(3*scr_height/4)), Image.ANTIALIAS)
scr_bg= ImageTk.PhotoImage(bg_image)

#image canvas
login_bg=tk.Canvas(my_login_window,bg="#88cffa",width=int(3/4*scr_width))
login_bg.pack(fill="both",expand=True)
login_bg.create_image(int(scr_width/2),int(scr_height/2.05),image=scr_bg,anchor="center")

#text
login_bg.create_text(int(scr_width/2),int(scr_height/6),font=("Helvetica",int(scr_width/32)),text="Login Page")

#login credentials
username_label=tk.Label(my_login_window,font=("Arial",int(scr_width/64)),text='Name')
password_label=tk.Label(my_login_window,font=("Arial",int(scr_width/64)),text='Password')

username=tk.Entry(my_login_window,width=int(scr_width/55),font=("default",int(scr_width/65)))
password=tk.Entry(my_login_window,width=int(scr_width/55),font=("default",int(scr_width/65)))

username.config(validate ="key", validatecommand =(reg, '% P'))
password.config(validate ="key", validatecommand =(reg, '% P'))

display_username_label=login_bg.create_window(int(scr_width/5),int(scr_height*2/5),window=username_label,anchor="center")
display_username=login_bg.create_window(int(scr_width*4/10),int(scr_height*2/5),window=username,anchor="center")
display_password_label=login_bg.create_window(int(scr_width/5),int(scr_height*1/2),window=password_label,anchor="center")
display_password=login_bg.create_window(int(scr_width*4/10),int(scr_height*1/2),window=password,anchor="center")

#single option buttons
btn_val=tk.StringVar(value="Student")

def btn_checked():
    global store_val
    store_val=btn_val

student_box=tk.Radiobutton(my_login_window,font=("default",int(scr_width/65)),text='Student',value='Student',variable=btn_val,command=lambda: btn_checked() )
Teacher_box=tk.Radiobutton(my_login_window,font=("default",int(scr_width/65)),text='Teacher',value='Teacher',variable=btn_val,command=lambda: btn_checked() )
Admin_box=tk.Radiobutton(my_login_window,font=("default",int(scr_width/65)),text='Admin',value='Admin',variable=btn_val,command=lambda: btn_checked() )

display_student_box=login_bg.create_window(int(scr_width*3/10),int(scr_height*4/7),window=student_box,anchor="center")
display_Teacher_box=login_bg.create_window(int(scr_width*4/10),int(scr_height*4/7),window=Teacher_box,anchor="center")
display_Admin_box=login_bg.create_window(int(scr_width*5/10),int(scr_height*4/7),window=Admin_box,anchor="center")


t=(store_username,store_password.get(),store_val)

#enter button
def final_check(p):
    if(valid_credentials(p)==True):
        my_login_window.destroy

login_btn=tk.Button(my_login_window,font=("Helvetica",int(scr_width/65),"underline"),text='LOGIN',bd='5',command=lambda:[print(11,t),final_check(t)])

display_login_btn=login_bg.create_window(int(scr_width*1/2),int(scr_height*5/7),window=login_btn,anchor="center")
my_login_window.mainloop()

print(entered_data)