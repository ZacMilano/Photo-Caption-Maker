import tkinter  # The GUI framework.
from date_to_day_of_week_calculator import *  # A file containing some functions
                                              # that I wrote for this project.

class Main_Window:
  def __init__(self):
    # Some colors that will be used. self.button_col has an extra (commented-
    # out) option; the difference isn't that extreme, though noticeable.
    self.main_bg = "#21252B"
    self.gui_text_col = "#9da5b4"
    self.button_col = "#30353e"  #"#282C34"

    # The main/only window. Use it wisely.
    self.master = tkinter.Tk()
    self.master.title("Mallory's Caption Maker <3")

    # Sets the background color of the window.
    self.master.configure(bg=self.main_bg)

    # Creation of widget elements.
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

    # Binds the return key to create a caption, when in the entry fields.
    self.person_entry.bind("<Return>", lambda x: self.add_caption(
      self.person_entry.get(),
      self.what_was_done_entry.get(),
      self.time_entry.get()
    ))
    self.what_was_done_entry.bind("<Return>", lambda x: self.add_caption(
      self.person_entry.get(),
      self.what_was_done_entry.get(),
      self.time_entry.get()
    ))
    self.time_entry.bind("<Return>", lambda x: self.add_caption(
      self.person_entry.get(),
      self.what_was_done_entry.get(),
      self.time_entry.get()
    ))

    # For use in adding captions with add_caption.
    self.highest_row_index = 1
    # For use in columnspan cases.
    self.total_columns = 6

    # Creates the button that is used to generate captions.
    self.action_button = tkinter.Button(self.master,
                                        text = "GO!",
                                        command=lambda: self.add_caption(
                                          self.person_entry.get(),
                                          self.what_was_done_entry.get(),
                                          self.time_entry.get()
                                        ),
                                        fg=self.gui_text_col,
                                        bg=self.button_col)

    # Placement of entry fields and their respective labels.
    self.person_label.grid(row=0, column=0, pady=10, padx = 10)
    # I added pady only to the first column because it stays like that
    # for the other columns.
    self.person_entry.grid(row=0, column=1, sticky="we", padx = 10)
    self.what_was_done_label.grid(row=0, column=2, padx = 10)
    self.what_was_done_entry.grid(row=0, column=3, sticky="we", padx = 10)
    self.time_label.grid(row=0, column=4, padx = 10)
    self.time_entry.grid(row=0, column=5, sticky="we", padx = 10)


    # Placement of button.
    # Button should span the window width and stretch accordingly.
    self.action_button.grid(row=1,
                            column=0,
                            sticky = "we",
                            columnspan=self.total_columns,
                            pady=5)

    # Makes the columns scale according to the window width.
    # Entry fields have double weight.
    self.master.columnconfigure(0, weight = 1)
    self.master.columnconfigure(1, weight = 2)
    self.master.columnconfigure(2, weight = 1)
    self.master.columnconfigure(3, weight = 2)
    self.master.columnconfigure(4, weight = 1)
    self.master.columnconfigure(5, weight = 2)

    # The main loop. Duh.
    self.master.mainloop()

  # Creates the font size changer and output entry upon first call, and adds a
  # caption to the output entry with font size from the changer upon every call.
  def add_caption(self, str_0, str_1, str_2):
    if not self.highest_row_index > 1:  # Checks if this function has been run.
      self.highest_row_index = 3        # Basically makes it say it's been run.

      # Creates the slider that changes the font size in the output field.
      self.font_size_slider = tkinter.Scale(self.master,
                                            from_=5,
                                            to=80,
                                            orient="horizontal",
                                            label="Font Size",
                                            bg=self.button_col,
                                            fg=self.gui_text_col,
                                            highlightthickness=0,
                                            relief="solid",
                                            sliderrelief="flat",
                                            tickinterval=5,
                                            command=(lambda x:
                                                     self.scale_to_font_size(x)))
                                                # PEP-8 line length compliancy :(
      # Sets the default value for the font size.
      self.font_size_slider.set(14)

      # Places the font size slider.
      self.font_size_slider.grid(row=self.highest_row_index-1,
                                 columnspan=self.total_columns,
                                 sticky="we")

      # Creates the output field for the captions.
      self.output_field = tkinter.Text(self.master,
                                   wrap="word",
                                   width=1,
                                   height=100,
                                   padx=5,
                                   pady=5,
                                   bg=self.gui_text_col)

      # Places the output field for the captions.
      # Should span the window width and stretch accordingly.
      self.output_field.grid(row=self.highest_row_index,
                             columnspan=self.total_columns,
                             sticky="swe")

    # Whether the function has been run yet or not, whatever is in the entry
    # fields is copied into a caption.
    self.output_field.insert(1.0,
                             "{} did {} on {}.\n".format(  # Change if needed.
                               str_0,
                               str_1,
                               determine_date(str_2)  # Used the other document!
                               )
                             )

  # Allows the font to be set dynamically. The scale (font_size_slider) calls
  # this function with its value as num.
  def scale_to_font_size(self,num):
    self.output_field.configure(font=(
      "Avenir",
      num,
      "italic",
      "bold"))

# An instance of the Main_Window class.
# Opens window automatically (because of mainloop()).
a = Main_Window()
