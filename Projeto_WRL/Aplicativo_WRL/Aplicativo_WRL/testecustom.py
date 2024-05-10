from customtkinter import *
from PIL import Image


jnl = CTk()
jnl.geometry("600x600")

set_appearance_mode("dark")
img = Image.open("click.png")

bot = CTkButton(master=jnl, text ="Clica ae", corner_radius=30,fg_color='#EE9572',hover_color = '#FFA07A', border_color="#8B5742", border_width=3, image = CTkImage(dark_image =img))

bot.place(relx=0.5,rely=0.5,anchor="center")
jnl.mainloop()

