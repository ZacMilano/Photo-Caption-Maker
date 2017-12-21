# Name of this document is now misleading. Client didn't need the day of week.

def parse_string(input):
  if not type(input) == str:
    print("Error in parse_string: input is not a string.")
    return -1
  splitting_chars = [" ", "/", "\\", "-", "_", "~", "."]
  output_list=[]
  for char in splitting_chars:
    output_list.append(input.split(char))

  iterator = len(output_list) - 1
  while iterator >= 0:
    if output_list[iterator][0] == input:
      output_list.pop(iterator)
    iterator -= 1
  output_list = output_list[0]

  return output_list

def determine_date(input_str):
  if not isinstance(input_str, str):
    print("Error in determine_date: input is not a string.")
    return -1
  for char in input_str:
    if char.isalpha():
      return input_str
  str_list = parse_string(input_str)
  for elt in str_list:
    if len(elt) == 4:
      year = elt
      str_list.remove(elt)
  month_dict = {
    1 : "Jan.",
    2 : "Feb.",
    3 : "Mar.",
    4 : "Apr.",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "Aug.",
    9 : "Sept.",
    10 : "Oct.",
    11 : "Nov.",
    12 : "Dec."
  }
  month = month_dict[int(str_list[0])]
  date_num = str_list[1]

  day = None

  return "{} {}, {}".format(month, date_num, year)


# print(determine_date("2012-12-12"))
