# import sys, os, re
#
# os.chdir("C:/Users/zmonr/Desktop/Program Save FIles/atom/Photo_Captions")
# """ This needs to be changed dynamically. It should use the directory of the
#     text file's location and/or the .exe file's location.
# """
#
# def main():
#   input_file = open("da_file.txt", "r+")
#   text = input_file.read()
#
#   print(text)
#
#   list_for_caption = text.split("\n")
#
#   for elt in list_for_caption:
#     if elt == '' or elt == ' ' or elt == None:
#       list_for_caption.remove(elt)
#
#   lines = len(list_for_caption)
#
#   for line in range(0, lines):
#     list_for_caption[line] = list_for_caption[line].split(" ")
#
#   output_captions = []
#   index = 0
#
#   for line in list_for_caption:
#     output_captions.append("%s did %s on %s." % (line[0], line[1], line[2]))
#     # input_file.write("\n")
#     # input_file.write(output_captions[index])
#     index += 1
#
#   print(list_for_caption)
#   print(output_captions)
"""
Basically everything above this was for static files providing input
information. Instead, I'm going to use a GUI and have the captions be typed
one-by-one. It's what the client would want/does want.
"""

import tkinter
from date_to_day_of_week_calculator import *

class Main_Window:
  def __init__(self):
    self.master = tkinter.Tk()
    self.master.title("Caption Maker")
    # self.master.geometry('{}x{}'.format(800, 50))

    self.person_label = tkinter.Label(self.master, text = "Who?")
    self.time_label = tkinter.Label(self.master, text = "When?")
    self.what_was_done_label = tkinter.Label(self.master, text = "What?")

    self.person_entry = tkinter.Entry(self.master)
    self.time_entry = tkinter.Entry(self.master)
    self.what_was_done_entry = tkinter.Entry(self.master)

    self.action_button = tkinter.Button(self.master, text = "GO!")

    self.person_label.grid(row=0, column=0, pady=10)  # No need to add pady to
    self.person_entry.grid(row=0, column=1, sticky = "we")  # every column in
    self.time_label.grid(row=0, column=2)                   # this row.
    self.time_entry.grid(row=0, column=3, sticky = "we")
    self.what_was_done_label.grid(row=0, column=4)
    self.what_was_done_entry.grid(row=0, column=5, sticky = "we")

    self.action_button.grid(row=2, column=0,
                            sticky = "we",
                            columnspan=6,
                            pady=5)

    self.master.columnconfigure(1, weight = 1)
    self.master.columnconfigure(3, weight = 1)
    self.master.columnconfigure(5, weight = 1)


    self.master.mainloop()

  def add_caption(str_0, str_1, str_2):
    pass


a = Main_Window()





#
