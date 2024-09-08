from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import tkinter as tk
import customtkinter as CTk
import secrets
import pyperclip

CTk.set_default_color_theme("dark-blue")

class Pass:
    def create_new(length, characters):
        global parol
        parol = "".join(secrets.choice(characters) for _ in range(length))
        return parol
        
class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("460x250")
        self.title("Password generator")
        self.resizable(False, False)
        
        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent", )
        self.password_frame.grid(row=0, column=0, padx=(10, 20), pady=(20, 0), sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=280)
        self.entry_password.grid(row=0, column=2, padx=(80, 0), ipady=1)

        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.password_length_slider = CTk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100, command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_length_entry = CTk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cb_digits_var = tk.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var, onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)
        self.cb_digits.select()

        self.cb_lower_var = tk.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var, onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)
        self.cb_lower.select()

        self.cb_upper_var = tk.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var, onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)
        self.cb_upper.select()

        self.cb_symbols_var = tk.StringVar()
        self.cb_symbols = CTk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbols_var, onvalue=punctuation, offvalue="")
        self.cb_symbols.grid(row=2, column=3)
        self.cb_symbols.select()
        
        self.btn_generate = CTk.CTkButton(master=self.settings_frame, text="GENERATE", width=160, command=self.set_password)
        self.btn_generate.grid(row=3, column=0, columnspan=3, padx=(0, 10), pady=22)

        self.btn_copyng = CTk.CTkButton(master=self.settings_frame, text="COPYNG", width=40, command=self.set_copyng)
        self.btn_copyng.grid(row=3, column=1, columnspan=4, padx=(20, 0), pady=22)
        
        self.password_length_slider.set(12)
        self.password_length_entry.insert(0, "12")
            
    def slider_event(self, value):
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() + self.cb_symbols_var.get())
        return chars
    
    def set_copyng(self):
        pyperclip.copy(parol)
        
    def set_password(self):
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, Pass.create_new(length=int(self.password_length_entry.get()), characters=self.get_characters()))
        
if __name__ == "__main__":
    app = App()
    app.mainloop()