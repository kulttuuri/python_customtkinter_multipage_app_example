import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Page2(tk.Frame):

  ##############
  # COMPONENTS #
  ##############

  labelTitle1 : ctk.CTkLabel = None

  labelCombo : ctk.CTkLabel = None
  combo : ctk.CTkComboBox = None

  textfieldExample : ctk.CTkEntry = None

  buttonBack : ctk.CTkButton = None
  buttonContinue : ctk.CTkButton = None

  ###################
  # STATE VARIABLES #
  ###################

  #############
  # FUNCTIONS #
  #############

  def proceed(self):
    print(f"In dropdown menu, user has selected value: {self.combo.get()}")

    self.app.show_page(3)

  #######################
  # INITIALIZE THE PAGE #
  #######################
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.app = app

    NORMALFONT = app.styles.get("NORMALFONT")
    LARGEFONT = app.styles.get("LARGEFONT")

    # Label
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    self.labelTitle1 = ctk.CTkLabel(master=self, text="Example Page 2", font = LARGEFONT)
    self.labelTitle1.place(relx=0.5, rely=0.07, anchor=tk.CENTER)

    # Example of a dropdown menu
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkComboBox
    self.labelDropdown = ctk.CTkLabel(master=self, text="Dropdown", font = NORMALFONT)
    self.labelDropdown.place(relx=0.33, rely=0.25, anchor=tk.CENTER)
    self.combo = ctk.CTkComboBox(master=self)
    self.combo.place(relx=0.33, rely=0.30, anchor=tk.CENTER)
    # To set the options for the dropdown menu:
    self.combo.configure(values = ["Option 1", "Option 2", "Option 3"])

    # Set the selected value to empty
    self.combo.set("")
    # To get the currently selected value:
    self.combo.get()

    # Example of a textfield
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkEntry
    self.labelText = ctk.CTkLabel(master=self, text="Text", font = NORMALFONT)
    self.labelText.place(relx=0.66, rely=0.25, anchor=tk.CENTER)
    self.textfieldExample = ctk.CTkEntry(master=self)
    self.textfieldExample.place(relx=0.66, rely=0.30, anchor=tk.CENTER)
    # To get the value of the textfield:
    self.textfieldExample.get()

    # Button to go back
    self.buttonBack = ctk.CTkButton(master=self, text="Back", command= lambda : app.show_page(1))
    self.buttonBack.place(relx=0.33, rely=0.5, anchor=tk.CENTER)

    # Button to continue
    self.buttonContinue = ctk.CTkButton(master=self, text="Continue", command= lambda : self.proceed())
    self.buttonContinue.place(relx=0.66, rely=0.5, anchor=tk.CENTER)