def determine_day(input):
  if not type(input) == str:
    print("Error in determine_day: input is not a string.")
    return -1
  splitting_chars = [" ", "/", "\\", "-", "_"]
  output_list=[]
  for char in splitting_chars:
    output_list.append(input.split(char))
  for n in range(len(output_list)):
    print(output_list[n])
    if output_list[n][0] == input:
      output_list.pop(n)
      print(n)
  return output_list

print(determine_day("hey there"))
