import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Page3(tk.Frame):
  
  ##############
  # COMPONENTS #
  ##############

  labelTitle1 : ctk.CTkLabel = None
  labelTitle2 : ctk.CTkLabel = None
  buttonContinue : ctk.CTkButton = None
  sliderLabel : ctk.CTkLabel = None
  slider : ctk.CTkSlider = None
  switch : ctk.CTkSwitch = None

  ###################
  # STATE VARIABLES #
  ###################

  # For controlling / containing the switch state
  switch_var = None

  #############
  # FUNCTIONS #
  #############

  def switch_event(self):
    print("switch toggled, current value: ", self.switch_var.get())

    # Example how to show or hide a widget
    # If the toggle is "on", place it at the center of the page
    # If the toggle is "off", place it at a position outside the page
    if (self.switch_var.get() == "on"):
      self.labelTitle2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    else:
      self.labelTitle2.place(relx=10, rely=10, anchor=tk.CENTER)

  #######################
  # INITIALIZE THE PAGE #
  #######################
  def __init__(self, parent, app):
    tk.Frame.__init__(self, parent)
    self.app = app

    LARGEFONT = app.styles.get("LARGEFONT")

    # Title label
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
    self.labelTitle1 = ctk.CTkLabel(master=self, text="Example Page 3", font = LARGEFONT)
    self.labelTitle1.place(relx=0.5, rely=0.07, anchor=tk.CENTER)

    # Example slider
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkSlider
    self.sliderLabel = ctk.CTkLabel(master=self, text="Slider")
    self.sliderLabel.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
    self.slider = ctk.CTkSlider(master=self, from_=0, to=100)
    self.slider.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    # To get the value of the slider:
    self.slider.get()

    # Example switch
    # https://github.com/TomSchimansky/CustomTkinter/wiki/CTkSwitch
    self.switch_var = ctk.StringVar(value="off")
    self.switch = ctk.CTkSwitch(master=self, text="Example of a switch that shows or hides another widget", command=self.switch_event, variable=self.switch_var, onvalue="on", offvalue="off")
    self.switch.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    # Label that gets visible if the switch is on
    self.labelTitle2 = ctk.CTkLabel(master=self, text="Switch is on", font = LARGEFONT)

    self.buttonContinue = ctk.CTkButton(master=self, text="Back", command=lambda : app.show_page(2))
    self.buttonContinue.place(relx=0.5, rely=0.5, anchor=tk.CENTER)