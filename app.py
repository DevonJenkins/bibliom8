import os
path = './'

def init():
  count = 0
  if not os.path.isdir("./records"):
    print("no such directory records.\n")
    print("creating records directory.\n")
    os.mkdir("records")

  input("press enter to continue\n")
  filename = input("enter a filename: \n") + ".txt" 
  main(count, filename)

def main(count, filename ):
  #create and open new file with chosen filename
  f = open(f"records/{filename}", "a")

  name = input("enter a name: ")

  count = count + 1

  #make function for writing into file
  f.write(f"{count}.{{\n")
  f.write(f"\tname: {name}\n")
  f.write(f"  }}\n")
  f.close()#is this necessary? more testing required

  confirmation(f, filename, count)


def confirmation(f, filename, count):
  #conf = confirmation 
  conf_input = input("Would you like to continue? [y] or [n]?\n")
  
  if conf_input == 'y' or  conf_input == 'Y':
    main(count, filename)

  elif conf_input == 'n' or conf_input == 'N':
    close_file(f, filename)

  else:
    print("Please enter a valid input")
    confirmation(f, filename, count)

def close_file(f, filename):
  f.close()
  #open text file
  os.system(f"open records/{filename}")

init()



