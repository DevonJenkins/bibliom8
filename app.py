import os

def init():
  count = 0
  filename = input("enter a filename: \n") + ".txt"
  main(count, filename)

def main(count, filename):
  #increase count
  f = open(filename, "a")

  name = input("enter a name: ")

  count = count + 1

  #make function for writing into file
  f.write(f"{count}.{{\n")
  f.write(f"name: {name}\n")
  f.write(f"}}\n")

  confirmation(f, filename, count)


def confirmation(f, filename, count):
  set_continue = False
  #conf = confirmation 
  conf_input = input("Would you like to continue? [y] or [n]?\n")
  
  if conf_input == 'y' or  conf_input == 'Y':
    set_continue == True
    main(count, filename)
    f.close

  elif conf_input == 'n' or conf_input == 'N':
    set_continue == False 
    #close file
    close_file(f, filename)

  else:
    print("Please enter a valid input")
    confirmation(f, filename, count)

def close_file(f, filename):
  f.close

  #open text file
  os.system(f"open {filename}")

init()


#note: it would be very nice spit my newly created files into a separate
#directory 

