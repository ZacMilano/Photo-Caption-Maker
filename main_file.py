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

def main():
  pass



if __name__ == "__main__":
  main()
