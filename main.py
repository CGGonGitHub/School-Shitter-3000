import tkinter
from tkinter import *
import tkinter.messagebox as messagebox
import customtkinter
import webbrowser
import os
import subprocess
import os
import winshell
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("SchoolShitter3000 - make your IT teacher cry")
        self.geometry(f"{1200}x{800}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=180)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nswe", padx=20, pady=20)
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="School Shitter 3000", text_color="red", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.logo_label2 = customtkinter.CTkLabel(self.sidebar_frame, text="make your IT teacher cry", font=customtkinter.CTkFont(size=11, weight="bold"))
        self.logo_label2.grid(row=0, column=0, padx=20, pady=(70, 10))
        self.sidebar_button1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_GitHub, text= "GitHub")
        self.sidebar_button1.grid(row=1, column=0, padx=20, pady=20)
        self.sidebar_button2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_Youtube, text= "Youtube Video")
        self.sidebar_button2.grid(row=2, column=0, padx=20, pady=20)
        self.sidebar_button3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_Discord, text= "Discord")
        self.sidebar_button3.grid(row=3, column=0, padx=20, pady=20)
        self.sidebar_footer = customtkinter.CTkLabel(self.sidebar_frame, text="No.9#5768", font=customtkinter.CTkFont(size=15))
        self.sidebar_footer.grid(row=6, column=0, padx=20, pady=10)

        # create Frame
        self.ButtonFrame = customtkinter.CTkFrame(self)
        self.ButtonFrame.grid(row=0, column=1, rowspan=3, sticky="nswe", padx=(0,20), pady=20)
        self.ButtonShutdownCustomMessage = customtkinter.CTkButton(self.ButtonFrame, command=self.shutdown, text="Shutdown")
        self.ButtonShutdownCustomMessage.grid(padx=20, pady=1)
        self.ButtonError = customtkinter.CTkButton(self.ButtonFrame, command=self.looperror, text="Loop Error")
        self.ButtonError.grid(padx=20, pady=5)
        self.RickRoll = customtkinter.CTkButton(self.ButtonFrame, command=self.rickrolltartupshortcut, text="RickRoll on startup")
        self.RickRoll.grid(padx=20, pady=1)
        # create Entry
        self.entry = customtkinter.CTkEntry(self, width=200)
        self.entry.grid(row=3, column=1, padx=(0,150), pady=(20,40), sticky="nsew")
        # create Submit Button
        self.SubmitButton = customtkinter.CTkButton(self, command=self.submit, text= "Submit & Run", fg_color="green")
        self.SubmitButton.grid(row=3, column=1, padx=(745,20), pady=(20,40), sticky="nsew")


    def sidebar_button_GitHub(self):
        webbrowser.open('https://github.com/CGGonGitHub/School-Shitter-3000')
    
    def sidebar_button_Youtube(self):
        webbrowser.open('https://www.youtube.com')
    
    def sidebar_button_Discord(self):
        webbrowser.open('https://discord.gg/kGJ6JvA8hT')
    
    def shutdown(self):
        os.system('shutdown /s /t 10 /c self.entry.get()')
    
    def looperror(self):
        tempval = True
        while (tempval):
            messagebox.showerror("Sorry :(", self.entry.get())
            
    def submit(self):
        print(self.entry.get())
    
    def rickrolltartupshortcut():
        startup = winshell.startup()
        path = os.path.join(startup, "RickRoll.url")
        target = "https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif"
        shortcut = file(path, 'w')
        shortcut.write('[InternetShortcut]\n')
        shortcut.write('URL=%s' % target)
        shortcut.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()
