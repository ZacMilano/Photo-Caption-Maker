import tkinter
from date_to_day_of_week_calculator import *

class Main_Window:
  def __init__(self):
    self.main_bg = "#21252B"
    self.gui_text_col = "#9da5b4"
    self.button_col = "#30353e"  #"#282C34"


    self.master = tkinter.Tk()
    self.master.title("Caption Maker")
    # self.master.geometry('{}x{}'.format(800, 50))
    self.master.configure(bg=self.main_bg)


    self.person_label = tkinter.Label(self.master,
                                      text="Who?",
                                      bg=self.main_bg,
                                      fg=self.gui_text_col)
    self.what_was_done_label = tkinter.Label(self.master,
                                             text = "What?",
                                             bg=self.main_bg,
                                             fg=self.gui_text_col)
    self.time_label = tkinter.Label(self.master,
                                    text = "When?",
                                    bg=self.main_bg,
                                    fg=self.gui_text_col)

    self.person_entry = tkinter.Entry(self.master, bg=self.gui_text_col)
    self.what_was_done_entry = tkinter.Entry(self.master, bg=self.gui_text_col)
    self.time_entry = tkinter.Entry(self.master, bg=self.gui_text_col)
    # Creation of widget elements

    self.highest_row_index = 1
    # For use in adding captions with add_caption
    self.total_columns = 6
    # For use in columnspan cases

    self.action_button = tkinter.Button(self.master,
                                        text = "GO!",
                                        command=lambda: self.add_caption(
                                          self.person_entry.get(),
                                          self.what_was_done_entry.get(),
                                          self.time_entry.get()
                                        ),
                                        fg=self.gui_text_col,
                                        bg=self.button_col)

    self.person_label.grid(row=0, column=0, pady=10, padx = 10)
    '''I added pady only to the first column because it stays like that
    for the other columns.'''
    self.person_entry.grid(row=0, column=1, sticky="we", padx = 10)
    self.what_was_done_label.grid(row=0, column=2, padx = 10)
    self.what_was_done_entry.grid(row=0, column=3, sticky="we", padx = 10)
    self.time_label.grid(row=0, column=4, padx = 10)
    self.time_entry.grid(row=0, column=5, sticky="we", padx = 10)




    self.action_button.grid(row=1, column=0,
                            sticky = "we",
                            columnspan=self.total_columns,
                            pady=5)

    self.master.columnconfigure(0, weight = 1)
    self.master.columnconfigure(1, weight = 2)
    self.master.columnconfigure(2, weight = 1)
    self.master.columnconfigure(3, weight = 2)
    self.master.columnconfigure(4, weight = 1)
    self.master.columnconfigure(5, weight = 2)
    # Makes the columns scale according to the window width



    self.master.mainloop()

  def add_caption(self, str_0, str_1, str_2):
    if not self.highest_row_index > 1:
      self.highest_row_index = 3
      self.font_size_slider = tkinter.Scale(self.master,
                                            from_=5,
                                            to=40,
                                            orient="horizontal",
                                            label="Font Size",
                                            bg=self.button_col,
                                            fg=self.gui_text_col,
                                            highlightthickness=0,
                                            relief="solid",
                                            sliderrelief="flat",
                                            tickinterval=5)
      self.font_size_slider.set(14)
      self.font_size_slider.grid(row=self.highest_row_index-1,
                                 columnspan=self.total_columns,
                                 sticky="we")
      self.new_text = tkinter.Text(self.master,
                                   wrap="word",
                                   width=50,
                                   height=10,
                                   padx=5,
                                   pady=5,
                                   font=("Avenir",
                                         self.font_size_slider.get(),
                                         "italic", "bold"),
                                   bg=self.gui_text_col)
      self.new_text.grid(row=self.highest_row_index,
                         columnspan=self.total_columns,
                         sticky="we")

    self.new_text.insert(1.0,
                         "{} did {} on {}.\n".format(
                           str_0, str_1, determine_day(str_2)
                         ))


a = Main_Window()





#
