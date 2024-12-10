import customtkinter
import tkinter
from tkinter import *
from combined import a
from server5 import startserver
no_of_images=1

def server():
    global no_of_images
    no_of_images=startserver()
def getimg():
    x=350
    y=200
    global img_list
    img_list = []  # Initialize an empty list to store PhotoImage objects
    for i in range(no_of_images):
        canvas = tkinter.Canvas(root, width=250, height=250)
        canvas.place(x=x, y=y)

        label = customtkinter.CTkLabel(master=root, text="ReceivedImage"+str(i+1))
        label.place(x=x+150, y=y)  # Adjusted x-coordinate to place the label to the right of the canvas

        img = tkinter.PhotoImage(file="ReceivedImage"+str(i+1)+".png")
        img = img.subsample(2)
        canvas.create_image(0, 0, anchor=tkinter.NW, image=img)
        img_list.append(img)  # Add the PhotoImage object to the list
        
        # Update coordinates for the next image
        y += 260  # Adjust as needed to leave space between images
    root.mainloop()

def dec():
    a(no_of_images)
    x=1200
    y=200
    global img1_list
    img1_list = []
    for i in range(no_of_images):
        canvas = tkinter.Canvas(root, width = 250, height = 250)
        canvas.place(x=x, y=y)
        label=customtkinter.CTkLabel(master=root,text="DecryptedImage"+str(i+1))
        label.place(x=x-350, y=y)  # Adjusted x-coordinate to place the label to the right of the canvas
        im = tkinter.PhotoImage(file="ReceivedImage"+str(i+1)+"CombinedDecrypted.png")
        im=im.subsample(2)
        canvas.create_image(0,0, anchor=tkinter.NW, image=im)
        img1_list.append(im)  # Add the PhotoImage object to the list
        y += 260  # Adjust as needed to leave space between images
    root.mainloop()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root=customtkinter.CTk()
root.geometry("1300x1300")  
root.title("Welcome to Server")
def x():
    
    def setup_gui():
        label=customtkinter.CTkLabel(master=root,text="Welcome to server ",text_color='violet',font=("TimesNewRoman",36,'bold'))
        label.pack(pady=2,padx=2)
        
        button=customtkinter.CTkButton(master=root,text="Start the server",command=server)
        button.pack(pady=10,padx=10)
        label=customtkinter.CTkLabel(master=root,text="Encrypted Image",text_color='violet',font=("TimesNewRoman",14,'bold'))
        label.place(x=105,y=100)
        # canvas = tkinter.Canvas(root, width = 250, height = 250)
        # canvas.pack()
        button=customtkinter.CTkButton(master=root,text="Get Encrypted",command=getimg)
        button.place(x=100,y=150)
        # img = tkinter.PhotoImage(file="ReceivedImage3.png")
        # img=img.subsample(2)
        # canvas.create_image(0,0, anchor=tkinter.NW, image=img)
        label=customtkinter.CTkLabel(master=root,text="Decrypted Image",text_color='violet',font=("TimesNewRoman",14,'bold'))
        label.place(x=1205,y=100)
        button=customtkinter.CTkButton(master=root,text="Decrypt image",command=dec)
        button.place(x=1200,y=150)
    setup_gui()
    root.mainloop()
    
x()