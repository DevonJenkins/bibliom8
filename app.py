import os
import platform
path = './'

def init():
  count = 0
  if not os.path.isdir("./records"):
    print("no such directory records.\n")
    print("creating records directory.\n")
    os.mkdir("records")

  greeting()
  filename = input("enter a filename: \n") + ".txt" 
  main(count, filename)

def greeting():
  greeting = input("press h for help. press enter to continue\n")

  if greeting == "h" or greeting == "H":
    help()



def main(count, filename ):

  #create and open new file with chosen filename
  f = open(f"records/{filename}", "a")

  author = input("enter author/s: ")
  title = input("enter the title: ")
  subtitle = input("enter the subtitle: ")
  isbn = input("enter the isbn: ")
  lccn = input("enter the lccn: ")
  publisher = input("enter the publisher/s: ")
  publish_date = input("enter the publishing date: ")

  count = count + 1

  #make function for writing into file
  write(f, count, author, title, subtitle, isbn, lccn, publisher, publish_date)

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
  #this function is named confusingly. It closes the file in python but then it
  # takes the steps to open the file in terminal

  f.close() #is this closefile necessary?
  #windows doesn't use the same file opening convention. 
    #I'll have to check the operating system. If the operating system is  
    # windows then i must change file opening command. 
  check_OS(filename)

def check_OS(filename):
  my_os = platform.system()
  print("OS in my system : ", my_os) # TODO delete this line for final production

  if my_os == "Windows":
    #change into records directory
    os.chdir('records')
    #open file from records directory
    os.system(filename)
  
  else:
    os.system(f"open records/{filename}")
    #this is currently based around mac and windows assuming that most
    #librarians aren't using linux

def write(f, count, author, title, subtitle, isbn, lccn, publisher, publish_date):
  f.write(f"{count}.{{\n")
  f.write(f"\tauthor: {author}\n")
  f.write(f"\ttitle: {title}\n")
  f.write(f"\tsubtitle: {subtitle}\n")
  f.write(f"\tisbn: {isbn}\n")
  f.write(f"\tlccn: {lccn}\n")
  f.write(f"\tpublisher: {publisher}\n")
  f.write(f"\tpublish date: {publish_date}\n")
  f.write(f"  }}\n")
  f.close() # This closefile is necessary

def help(): 
  print("here is some help, friend")

  print("to cancel at any time, press ctrl-c")

  greeting()

#create function for clean exit of the app. 
  #while app is running, if user types exit, then close the app. 

init()



