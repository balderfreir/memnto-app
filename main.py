import tkinter
import customtkinter as ctk
from data import df



ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

window = tkinter.Tk()  # create the Tk window like you normally do
window.geometry("500x400")
window.title("FlashApp")


def button_function():
    global current_word
    current_word = df.sample()
    label.configure(text=current_word.iloc[0][0])

def button_function2():
    label.configure(text=current_word.iloc[0][1])

# Use CTkButton instead of tkinter Button
button_right = ctk.CTkButton(master=window, text="know", corner_radius=10, command=button_function)
button_right.place(relx=0.2, rely=0.9, anchor=tkinter.CENTER)

button_wrong = ctk.CTkButton(master=window, text="don't know", corner_radius=10, command=button_function2)
button_wrong.place(relx=0.8, rely=0.9, anchor=tkinter.CENTER)

# CTkFrame
frame = ctk.CTkFrame(master=window,
                     width=400,
                     height=250,
                     corner_radius=10)
frame.pack(padx=20, pady=20)

label = ctk.CTkLabel(master=frame, text="CTkLabel")
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

window.mainloop()