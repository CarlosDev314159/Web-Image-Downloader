import wget, os
from tkinter import Tk, filedialog
from colorama import Fore, init 

# importing libs

# To close another extra window opened by tkinter
close_window = Tk()
close_window.withdraw()

# Remove coloring at the end of each print
init(autoreset=True)

# the list that will store the links
images = []

while True:
    url = input("Press '0' to exit the program or Press '1' to go to downloads.\nPaste the link here:\n")
    if url == "0":
          exit()
    elif url != "1":
          images.append(url)
    else:
         path = filedialog.askdirectory(title="Where would you like to save?") # Open the directory to choose where to save
         try:
              if path == ():
                 os.chdir(path) #switch to the chosen path
         except TypeError as e:
                 print(Fore.RED + "Canceled by user\n")
                 exit()
         try:
             for link in images:
                download = wget.download(link)
                print("\n")
                print(Fore.GREEN + "Download successful!")
                exit()
         except ValueError as e:
                print(f"{Fore.RED}Download failed!\n{Fore.YELLOW}Error log: {e}")
                exit()