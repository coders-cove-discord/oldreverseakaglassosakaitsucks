import time
import os
import shell
import commands
import kernel
import gpm

os.system("cls")

print("Booting...")

time.sleep(1)

print("""  
   _____ _                  ____   _____ 
  / ____| |                / __ \ / ____|
 | |  __| | __ _ ___ ___  | |  | | (___  
 | | |_ | |/ _` / __/ __| | |  | |\___ \ 
 | |__| | | (_| \__ \__ \ | |__| |____) |
  \_____|_|\__,_|___/___/  \____/|_____/
                                          """)
time.sleep(1)

shell.init()